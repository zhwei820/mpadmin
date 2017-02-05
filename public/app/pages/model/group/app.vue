<template>
  <div>
    <el-button type="primary" @click="createNewLayer">新建</el-button>
    <el-button type="primary" icon="more" class="right_export" @click="saveExcel"></el-button>
    <el-input placeholder="搜索" class="right_search" icon="search" v-model="input2" @click="handleSearch" @keyup.enter.native="handleSearch">
    </el-input>
    <el-table :data="tableData" border style="width: 100%" height="920">
      <el-table-column fixed :context="_self" inline-template label="操作" width="150">
        <div>
          <el-button size="small" @click="handleEdit($index, row)">
            编辑
          </el-button>
          <el-button size="small" type="danger" @click="handleDelete($index, row)">
            删除
          </el-button>
        </div>
      </el-table-column>
      <el-table-column prop="name" :label=tableHead.name width="120">
      </el-table-column>
      <el-table-column prop="layer_name" :label=tableHead.layer_name width="120">
      </el-table-column>
    </el-table>
    <div class="block">
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="tablePage" :page-sizes="[100, ]"
        :page-size="pageSize" layout="total, sizes, prev, pager, next, jumper" :total="totalNum">
        </el-pagination>
    </div>
    <el-dialog title="CI模型组编辑" v-model="dialogFormVisible">
      <el-form>
        <el-form-item label="CI模型组名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="CI模型层" :label-width="formLabelWidth">
          <el-select v-model="form.layer" placeholder="请选择">
            <el-option v-bind:label="index" v-bind:value="item" v-for="(item, index) in layer_list">
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
  import {
    excel,
    deepCopyOfObject

  } from "../../../assets/js/util.js"

  export default {
    data() {
      return {
        input2: "",
        tableHead: {
          "name": "组名称",
          "layer": "层",
          "layer_name": "层名称",
        },
        tableHeadKeys: [
          "name",
          "layer",
          "layer_name",
        ],
        tableData1: [],
        tableData: [],
        tablePage: 1,
        pageSize: 100,
        totalNum: 1,

        dialogFormVisible: false,
        form: {
          name: '',
          id: "",
          layer: "default",
        },
        layer_list: {},
        layer_name_list: {},
        formLabelWidth: '120px',
      }
    },

    beforeMount: function () {
      
      this.get_layer_list()
    },
    methods: {
      get_layer_list() {
        var query = ""
        this.$http.get("/api/layers/" + query).then((response) => {
          if (response.status !== 200) {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          }
          this.layer_list = {}
          for (var key in response.data) {
            this.layer_list[response.data[key].name] = response.data[key].id;
          }
          this.layer_name_list = {}
          for (var key in response.data) {
            this.layer_name_list[response.data[key].id] = response.data[key].name;
          }
          this.fetch(0, 100)
        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        });
      },
      fetch(offset, limit) {
        this.$http.get("/api/groups/?offset=" + offset + "&limit=" + limit).then((response) => {
          if (response.status !== 200) {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          }
          var res = response.data
          for (var key in res) {
            res[key].layer_name = this.layer_name_list[res[key].layer];
          }
          this.tableData = res
          this.tableData1 = res
          this.totalNum = this.tableData1.length
        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        });
      },
      submit() {
        if (!this.form.id) {
          this.$http.post("/api/groups/", this.form).then((response) => {}, (response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });
        } else {
          this.$http.put("/api/groups/" + this.form.id + "/", this.form).then((response) => {}, (
            response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });

        }
        this.dialogFormVisible = false
        this.fetch(0, 100)
      },

      handleEdit(index, row) {
        console.log(index, row);
        this.form = deepCopyOfObject(row)

        this.dialogFormVisible = true;
      },
      createNewLayer() {
        this.dialogFormVisible = true
        this.form = {
          "name": "",
          "layer": this.layer_list.default,
          "id": "",
        }
      },
      handleDelete(index, row) {
        console.log(index, row);
      },

      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      handleSearch(ev) {
        if (this.input2) {
          var tmp = []
          for (var ii = 0; ii < this.tableData1.length; ii++) {
            for (var jj in this.tableData1[ii]) {
              if (("" + this.tableData1[ii][jj]).indexOf(this.input2) >= 0) {
                tmp.push(this.tableData1[ii])
                break
              }
            }
          }
          this.tableData = tmp
        } else {
          this.tableData = this.tableData1
        }
        // this.totalNum = this.tableData.length
      },
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        console.log(val);
        console.log(`当前页: ${val}`);
        // this.tableData = this.tableData1.slice((val - 1) * this.pageSize, (val) * this.pageSize)

        this.fetch((val - 1) * this.pageSize, this.pageSize)
      },
      saveExcel() {
        excel([this.tableHead].concat(this.tableData1), this.tableHeadKeys, "aaa", "xls")
      }
    }
  }
</script>
<style scoped>
  @import '../../../assets/css/normalize.css';
  .right_search {
    float: right;
    width: 20%;
  }
  
  .right_export {
    float: right;
  }
</style>