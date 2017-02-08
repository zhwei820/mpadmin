<template>
  <div v-if="id">
    <el-button type="primary" size="large" @click="createNewCIItem()">新建</el-button>
    <el-date-picker v-model="param.start_time" type="date" placeholder="开始日期" :picker-options="pickerOptions0">
    </el-date-picker>
    <el-date-picker v-model="param.end_time" type="date" placeholder="结束日期" :picker-options="pickerOptions0">
    </el-date-picker>
    <el-select v-model="param.value" placeholder="请选择">
      <!--<el-option v-for="item in options" :label="item.label" :value="item.value">
      </el-option>-->
    </el-select>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
    <el-button type="default" class="fa fa-refresh" @click="refresh_data"></el-button>
    <el-button type="primary" class="r fa fa-share-square-o" @click="saveExcel"></el-button>
    <el-input placeholder="搜索" class="right_search" icon="search" v-model="input2" @click="handleIconClick" @keyup.enter.native="handleIconClick">
    </el-input>
    <el-table :data="tableData" border style="width: 100%" height="920">
      <el-table-column fixed :context="_self" inline-template label="操作" width="150">
        <div>
          <el-button size="small" @click="handleEdit($index, row)">
            编辑
          </el-button>
          <el-button size="mini" type="danger" @click="handleDelete($index, row)">
            删除
          </el-button>
        </div>
      </el-table-column>
      <el-table-column prop="name" :label=tableHead.name width="120">
      </el-table-column>
      <!--<el-table-column prop="group_name" :label=tableHead.group_name width="120">
      </el-table-column>-->
    </el-table>
    <div class="block">
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="tablePage" :page-sizes="[20, 50, 100, 200, 400]"
        :page-size="pageSize" layout="total, sizes, prev, pager, next, jumper" :total="totalNum">
        </el-pagination>
    </div>
    <el-dialog title="" v-model="dialogFormVisible">
      <h2><span v-if="id">编辑</span><span v-else>新建</span> {{CIItem._category.name}} </h2>
      <el-form :model="CIItem" label-position="left">
        <el-form-item label="名称" :label-width="formLabelWidth">
          <el-input v-model="CIItem.name" auto-complete="off"></el-input>
        </el-form-item>
        <div v-for="(v, index_cpg) in CIItem._category.structure" v-if="index_cpg != 'hidden' && v.length > 0">
          <el-button @click="fold_cpg(index_cpg)" type="nomal" size="mini">
            <i :class="{'fa':true, 'fa-plus':CIItem._category.structure['hidden'][index_cpg], 'fa-minus': !CIItem._category.structure['hidden'][index_cpg]}"></i>
          </el-button>
          {{index_cpg}} 组
          <div v-if="! CIItem._category.structure['hidden'][index_cpg]">
            <el-form-item :label="v1.name" :label-width="formLabelWidth" v-for="v1 in v">
              <div v-if="v1.field != 'select' && v1.field != 'multi_select' && v1.field != 'datetime'">
                <el-input :type="v1.field == 'number'?'number':'text'" v-model="CIItem[v1.key]" auto-complete="off"></el-input><span v-if="v1.field == 'number'"> {{v1.unit}}</span>
              </div>
              <!--<div v-if="v1.field == 'select'">
                <select v-model="CIItem[v1.key]" :class="{'form-control':true}">
                  <option v-for="item in v1._choice" v-bind:value="item">
                    {{ item }}
                  </option>
                </select>
              </div>-->
              <div v-if="v1.field == 'multi_select' || v1.field == 'select'">
                <el-select v-model="CIItem[v1.key]" :multiple="v1.field == 'multi_select'">
                  <el-option v-for="item in v1._choice" v-bind:value="item">
                    {{ item }}
                  </el-option>
                </el-select>
              </div>
              <div v-if="v1.field == 'datetime'">
                <el-date-picker v-model="CIItem[v1.key]" type="datetime" placeholder="选择日期时间">
                </el-date-picker>
              </div>
              类型：{{fields_comment[v1.field]}}, <span v-if="v1.field == 'string' || v1.field == 'number'">最大/最长： {{v1.max}}, 最小: {{v.min}}, </span>
            </el-form-item>
          </div>
        </div>
        <div class="ci_prop_group" v-for="(ci_prop_group, index_cpg) in CIItem.structure">
        </div>
      </el-form>
      <div class="dialog-footer">
        <el-row type="flex" class="row-bg" justify="end">
          <el-button type="primary" @click="submit">确 定</el-button>
        </el-row>
      </div>
    </el-dialog>
  </div>
</template>
<script>
  import {
    excel,
    json2url,
    Vue,
    deepCopyOfObject
  } from "../../assets/js/util.js"

  export default {
    data() {
      return {
        pickerOptions0: {
          disabledDate(time) {
            return time.getTime() < Date.now() - 8.64e7;
          }
        },
        dialogTableVisible: false,
        id: false,
        param: {
          start_time: (new Date((new Date()).setDate(new Date().getDate() - 1))),
          end_time: (new Date()),
          name: "",
          value: '',
        },
        input2: "",
        tableHead: {
          "name": "CI模型实例名称",
          group_name: "CI模型分组名称",
        },
        tableHeadKeys: [
          "date",
          "name",
          "group_name",
        ],
        tableData1: [],
        tableData: [],
        tablePage: 1,
        pageSize: 20,
        totalNum: 1,

        dialogFormVisible: false,
        formLabelWidth: '120px',

        CIItem: {
          "name": "",
          "id": "",
          _category: {
            name: ""
          },
        },
        // tmp_key: "",
        // tmp_name: "",
        // tmp_group: "default",
        field: "",
        cpg_list: {
          default: ""
        },
        item_category: {},
        field_list: {},
        fields_comment: {},
      }
    },
    beforeMount: function () {
      window.vm_n = this
      this.fetch(0, this.pageSize);
      this.get_field_list()
    },
    methods: {
      get_field_list() {
        var query = ""
        this.$http.get("/api/field_list" + query).then((response) => {
          if (response.status !== 200) {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          }
          this.field_list = response.data['field_list']
          this.fields_comment = response.data['fields_comment']
        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        });
      },
      get_item_category() {
        this.$http.get("/api/items_categories/" + this.id).then((response) => {
          this.item_category = response.data

          for (var key in this.item_category.structure) {
            var element = this.item_category.structure[key];

            for (var key1 in element) {
              if (element[key1].field != undefined && (element[key1].field == "select" || element[key1].field ==
                  "multi_select")) {
                this.item_category.structure[key][key1]._choice = this.item_category.structure[key][key1].choice.split(
                  "|")
              }
            }
          }

        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        });
      },
      fetch() {
        var id = this.$route.params.id
        this.id = id == undefined ? "" : id

        if (this.id) {
          this.$http.get("/api/items_categories/" + this.id + '/items').then((response) => {
            var res = response.data
            this.tableData1 = res
            this.tableData = this.tableData1.slice(0, this.pageSize)
            this.totalNum = this.tableData1.length
            this.get_item_category()
          }, (response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });
        }
      },
      handleEdit(index, row) {
        var _CIItem = deepCopyOfObject(row)

        _CIItem._category = this.item_category,
          this.dialogFormVisible = true
        for (var key in this.item_category.structure) {
          var element = this.item_category.structure[key];
          for (var key1 in element) {

            if (element[key1].field == "multi_select" && typeof (_CIItem[element[key1].key]) == "string") {
              _CIItem[element[key1].key] = [_CIItem[element[key1].key]]
            }
          }
        }
        this.CIItem = _CIItem
        console.log(this.CIItem);

      },
      createNewCIItem() {
        this.dialogFormVisible = true
        var _CIItem = {
          "name": "234",
          "id": "",
          _category: this.item_category,
          category: this.id,
        }
        for (var key in this.item_category.structure) {
          var element = this.item_category.structure[key];
          for (var key1 in element) {
            if (element[key1].field == "multi_select") {
              element[key1].default = [this.item_category.structure[key][key1]._choice[0]] //multi_select 默认是array
            }
            if (element[key1].key != undefined) {
              _CIItem[element[key1].key] = element[key1].default || ''
            }
          }
        }
        this.CIItem = _CIItem
      },
      handleDelete(index, row) {
        this.$confirm('此操作将永久删除' + row.name + ', 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http.delete("/api/items/" + row.id + "/").then((response) => {
            this.dialogFormVisible = false
            this.fetch()
          }, (response) => {
            parent.vm.show_error_message(response.data.error)
          });
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      submit() {
        var ci_item = deepCopyOfObject(this.CIItem)
        delete ci_item._category
        if (!this.CIItem.id) {
          delete ci_item.id
          this.$http.post("/api/items/", ci_item).then((response) => {
            this.dialogFormVisible = false
            this.fetch()
          }, (response) => {
            parent.vm.show_error_message(response.data.error)
          });
        } else {
          this.$http.put("/api/items/" + this.CIItem.id + "/", ci_item).then((response) => {
            this.dialogFormVisible = false
            this.fetch()
          }, (response) => {
            parent.vm.show_error_message(response.data.error)
          });
        }
      },
      handleIconClick(ev) {
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
        console.log(`当前页: ${val}`);
        this.tableData = this.tableData1.slice((val - 1) * this.pageSize, (val) * this.pageSize)
      },
      saveExcel() {
        excel([this.tableHead].concat(this.tableData1), this.tableHeadKeys, "aaa", "xls")
      },
      refresh_data() {
        this.fetch(0, this.pageSize)

      },
      fold_cpg(e) {
        if (this.CIItem._category.structure['hidden'][e]) {
          this.CIItem._category.structure['hidden'][e] = false
        } else {
          this.CIItem._category.structure['hidden'][e] = true
        }
      }
    }
  }
</script>
<style scoped>
  @import '../../assets/css/normalize.css';
  @import '../../assets/css/index.css';
  .right_search {
    float: right;
    width: 20%;
  }
  
  .el-date-editor+.el-select {
    width: 120px;
  }
  
  .el-input {
    width: 250px;
  }
  
  .inline {
    display: inline-block;
  }
  
  .index_cpg {
    font-weight: 700;
  }
  
  .prop_label {
    display: inline-block;
    width: 20%;
  }
  
  .multi_select {
    height: 200px
  }
</style>