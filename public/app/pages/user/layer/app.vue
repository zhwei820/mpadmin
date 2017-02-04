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
    </el-table>
    <div class="block">
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="tablePage" :page-sizes="[100, ]"
        :page-size="pageSize" layout="total, sizes, prev, pager, next, jumper" :total="totalNum">
        </el-pagination>
    </div>
    <el-dialog title="CI模型层编辑" v-model="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="CI模型层名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" auto-complete="off"></el-input>
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
          "name": "层名称",
        },
        tableHeadKeys: [
          "name",
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
        },
        formLabelWidth: '120px',
      }
    },

    beforeMount: function () {
      this.fetch(0, 100)
    },
    methods: {
      fetch(offset, limit) {
        this.$http.get("/api/layers?offset=" + offset + "&limit=" + limit).then((response) => {
          if (response.status !== 200) {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          }
          var res = response.data
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
          this.$http.post("/api/layers/", this.form).then((response) => {}, (response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });
        } else {
          this.$http.put("/api/layers/" + this.form.id + "/", this.form).then((response) => {}, (
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