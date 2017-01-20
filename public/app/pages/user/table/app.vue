<template>
  <div>
    <el-button type="primary" @click="dialogFormVisible = true">新建</el-button>
    <el-date-picker v-model="param.start_time" type="date" placeholder="开始日期" :picker-options="pickerOptions0">
    </el-date-picker>
    <el-date-picker v-model="param.end_time" type="date" placeholder="结束日期" :picker-options="pickerOptions0">
    </el-date-picker>
    <el-select v-model="param.value" placeholder="请选择">
      <el-option v-for="item in options" :label="item.label" :value="item.value">
      </el-option>
    </el-select>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
    <el-input placeholder="姓名" v-model="param.name">
    </el-input>
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
      <el-table-column fixed prop="date" :label=tableHead.date width="150">
      </el-table-column>
      <el-table-column prop="name" :label=tableHead.name width="120">
      </el-table-column>
      <el-table-column prop="province" :label=tableHead.province width="120">
      </el-table-column>
      <el-table-column prop="city" :label=tableHead.city width="120">
      </el-table-column>
      <el-table-column prop="address" :label=tableHead.address width="300">
      </el-table-column>
      <el-table-column prop="zip" :label=tableHead.zip width="120">
      </el-table-column>
    </el-table>
    <div class="block">
      <!--<span class="demonstration">完整功能</span>-->
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="tablePage" :page-sizes="[20, 50, 100, 200, 400]"
        :page-size="pageSize" layout="total, sizes, prev, pager, next, jumper" :total="totalNum">
        </el-pagination>
    </div>
    <el-dialog title="收货地址" v-model="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="活动名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="活动区域" :label-width="formLabelWidth">
          <el-select v-model="form.region" placeholder="请选择活动区域">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
  import {
    excel,
    json2url
  } from "../../../assets/js/util.js"

  export default {
    data() {
      return {
        pickerOptions0: {
          disabledDate(time) {
            return time.getTime() < Date.now() - 8.64e7;
          }
        },
        options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        param: {
          start_time: (new Date((new Date()).setDate(new Date().getDate() - 1))),
          end_time: (new Date()),
          name: "",

          value: '',
        },
        input2: "",
        tableHead: {
          "date": "日期",
          "name": "姓名",
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
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        formLabelWidth: '120px',
      }
    },

    beforeMount: function () {
      this.fetch(0, this.pageSize)
    },
    methods: {
      fetch() {
        // console.log(this.param);

        var query = json2url(this.param)
        
        this.$http.get("/api/layers/?" + query).then((response) => {
          debugger
          if (response.status !== 200) {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          }
          var res = JSON.parse(response.data)
          this.tableData1 = res['data']
          this.tableData = this.tableData1.slice(0, this.pageSize)
          this.totalNum = this.tableData1.length
        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        });
      },
      handleEdit(index, row) {
        console.log(index, row);
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
        // this.fetch(0, this.pageSize)

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
</style>