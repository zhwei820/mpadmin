<template>
  <div>
    <el-button type="primary" @click="createNewCategory">新建</el-button>
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
          <el-button size="small" type="danger" @click="handleDelete($index, row)">
            删除
          </el-button>
        </div>
      </el-table-column>
      <el-table-column prop="name" :label=tableHead.name width="120">
      </el-table-column>
      <!--<el-table-column prop="province" :label=tableHead.province width="120">
      </el-table-column>
      <el-table-column prop="city" :label=tableHead.city width="120">
      </el-table-column>
      <el-table-column prop="address" :label=tableHead.address width="300">
      </el-table-column>
      <el-table-column prop="zip" :label=tableHead.zip width="120">
      </el-table-column>-->
    </el-table>
    <div class="block">
      <!--<span class="demonstration">完整功能</span>-->
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="tablePage" :page-sizes="[20, 50, 100, 200, 400]"
        :page-size="pageSize" layout="total, sizes, prev, pager, next, jumper" :total="totalNum">
        </el-pagination>
    </div>
    <el-dialog title="CI模型编辑" v-model="dialogFormVisible">
      <el-form :model="CICategory" label-position="left">
        <el-form-item label="CI模型名称" :label-width="formLabelWidth">
          <el-input v-model="CICategory.name" auto-complete="off"></el-input>
        </el-form-item>
        <div class="ci_prop_group" v-for="(ci_prop_group, index_cpg) in CICategory.structure">
          <div class="index_cpg" v-if="index_cpg != 'hidden'">
            <el-button @click="fold_cpg(index_cpg)" type="nomal" size="mini"> <i :class="{'fa':true, 'fa-plus':CICategory.structure['hidden'][index_cpg], 'fa-minus': !CICategory.structure['hidden'][index_cpg]}"></i>              </el-button>
            {{index_cpg}}组
            <div v-if="! CICategory.structure['hidden'][index_cpg]">
              <el-form-item v-bind:label="item.name" :label-width="formLabelWidth" v-for="(item, index) in ci_prop_group">
                <el-tooltip class="item" effect="dark" content="删除!" placement="top-start">
                  <el-button @click="delStructure(index_cpg, index)" type="danger" icon="minus" size="mini" class="del_btn"></el-button>
                </el-tooltip>
                <div v-for="(v, i) in item" v-if="">
                  <div v-if="i!='name' && i!='key' && i != 'field'">
                    <div class="prop_label">{{ fields_comment[i] }}</div>
                    <el-switch v-if="i=='required'" on-text="" off-text="" v-model="CICategory.structure[index_cpg][index][i]"></el-switch>
                    <el-input v-else-if="i=='min' || i=='max' " type="number" v-model="CICategory.structure[index_cpg][index][i]" auto-complete="off"></el-input>
                    <el-input v-else v-model="CICategory.structure[index_cpg][index][i]" auto-complete="off"></el-input>
                  </div>
                  <div v-if="i == 'field'">
                    <div class="prop_label">类型</div>
                    <el-input v-model="fields_comment[v]" auto-complete="off" disabled></el-input>
                  </div>
                  <div v-if="i=='name'||i=='key'">
                    <el-input v-if="i!='required' " v-model="CICategory.structure[index_cpg][index][i]" auto-complete="off" hidden></el-input>
                  </div>
                </div>
              </el-form-item>
            </div>
          </div>
        </div>
        <!--
        <el-form-item label="活动区域" :label-width="formLabelWidth">
          <el-select v-model="CICategory.region" placeholder="请选择活动区域">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select> 
        </el-form-item>-->
        <el-form-item label="添加属性" :label-width="formLabelWidth">
          <div class="inline">
            <div>名称</div>
            <el-input v-model="tmp_name" auto-complete="off"></el-input>
          </div>
          <div class="inline">
            <div>关键字</div>
            <el-input v-model="tmp_key" auto-complete="off"></el-input>
          </div>
          <div class="inline">
            <div>分组(可动态添加)</div>
            <el-select v-model="tmp_group" allow-create filterable="" placeholder="请选择分组">
              <!--<el-option label="default" value="default"></el-option>-->
              <el-option v-bind:label="index" v-bind:value="index" v-for="(item, index) in cpg_list">
              </el-option>
            </el-select>
          </div>
          <div>
            <div>类型</div>
            <el-select v-model="field" placeholder="请选择">
              <el-option v-bind:label="item.name" v-bind:value="index" v-for="(item, index) in field_list">
              </el-option>
            </el-select>
            <el-button @click="addStructure"><i class="fa fa-plus"></i></el-button>
          </div>
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
    json2url,
    Vue,
    deepCopyOfObject
  } from "../../../assets/js/util.js"

  export default {
    data() {
      return {
        pickerOptions0: {
          disabledDate(time) {
            return time.getTime() < Date.now() - 8.64e7;
          }
        },

        param: {
          start_time: (new Date((new Date()).setDate(new Date().getDate() - 1))),
          end_time: (new Date()),
          name: "",
          value: '',
        },
        input2: "",
        tableHead: {
          "name": "CI模型名称",
          "test": "test",
          "province": "省份",
          "city": "市区",
          "address": "地址",
          "zip": "邮编",
        },
        tableHeadKeys: [
          "date",
          "name",
          "test",
          "province",
          "city",
          "address",
          "zip",
        ],
        tableData1: [],
        tableData: [],
        tablePage: 1,
        pageSize: 20,
        totalNum: 1,

        dialogFormVisible: false,
        formLabelWidth: '120px',

        CICategory: {
          "name": "",
          "id": "",
          structure: {
            default: [],
            hidden: {
              default: false
            }
          },
        },
        tmp_key: "",
        tmp_name: "",
        tmp_group: "default",
        field_list: {},
        fields_comment: {},
        field: "",
        cpg_list: {
          default: ""
        },
      }
    },

    beforeMount: function () {
      this.fetch(0, this.pageSize)
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
          console.log(response.data)
          // var res = JSON.parse(response.data)
          this.field_list = response.data['field_list']
          this.fields_comment = response.data['fields_comment']
        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        });
      },
      fetch() {
        // console.log(this.param);
        var query = json2url(this.param)
        this.$http.get("/api/items_categories/?" + query).then((response) => {
          if (response.status !== 200) {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          }

          this.tableData1 = response.data
          this.tableData = this.tableData1.slice(0, this.pageSize)
          this.totalNum = this.tableData1.length
        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        });
      },
      addStructure() {
        var tmp = {}
        for (var k in this.field_list[this.field].properties) {
          tmp[k] = "";
        }
        tmp['field'] = this.field;
        tmp['name'] = this.tmp_name;
        tmp['key'] = this.tmp_key;

        this.tmp_name = ""
        this.tmp_key = ""

        if (this.CICategory.structure[this.tmp_group] == undefined) {
          this.CICategory.structure[this.tmp_group] = []
        }

        this.CICategory.structure[this.tmp_group].push(tmp)
        this.CICategory.structure['hidden'][this.tmp_group] = false
        this.tmp_group = "default"
        // console.log(this.CICategory.structure.default)
      },
      delStructure(g, i) {
        this.CICategory.structure[g].splice(i, 1)
      },
      submit() {
        if (!this.CICategory.id) {
          this.$http.post("/api/items_categories/", this.CICategory).then((response) => {}, (response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });
        } else {
          this.$http.put("/api/items_categories/" + this.CICategory.id + "/", this.CICategory).then((response) => {}, (
            response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });

        }
        this.dialogFormVisible = false
        this.refresh_data()
      },

      handleEdit(index, row) {
        row.structure['hidden'] = {}
        for (var key in row.structure) {
          row.structure['hidden'][key] = false;
          if (key != "hidden") {
            this.cpg_list[key] = ""
          }
        }
        this.CICategory = deepCopyOfObject(row)
        this.dialogFormVisible = true
        // console.log(index, row);
      },
      createNewCategory() {
        this.dialogFormVisible = true
        this.CICategory = {
          "name": "",
          "id": "",
          structure: {
            default: [],
            hidden: {
              default: false
            }
          },
        }
      },
      handleDelete(index, row) {
        console.log(index, row);
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
        if (this.CICategory.structure['hidden'][e]) {
          this.CICategory.structure['hidden'][e] = false
        } else {
          this.CICategory.structure['hidden'][e] = true
        }
      }
    }
  }
</script>
<style scoped>
  @import '../../../assets/css/normalize.css';
  @import '../../../assets/css/index.css';
  .right_search {
    float: right;
    width: 20%;
  }
  
  .el-date-editor+.el-select {
    width: 120px;
  }
  
  .el-input {
    width: 150px;
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
  
  .del_btn {
    border-radius: 20px;
    width: 25px;
    height: 25px;
  }
</style>