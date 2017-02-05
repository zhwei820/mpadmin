<template>
  <div>
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="6">
        <h2>CI模型组编辑</h2>
        <el-form label-position="top">
          <el-form-item label="CI模型组名称">
            <el-input v-model="form.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="CI模型层">
            <el-select v-model="form.layer" placeholder="请选择">
              <el-option v-bind:label="index" v-bind:value="item" v-for="(item, index) in layer_list">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <div class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="submit">确 定</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import {
    excel,
    deepCopyOfObject,
    paramParse

  } from "../../../assets/js/util.js"

  export default {
    data() {
      return {
        input2: "",

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
        var id = paramParse('id')
        this.$http.get("/api/groups/" + id + "/").then((response) => {

          if (response.status !== 200) {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          }
          this.form = response.data

        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        });
      },
      submit() {
        if (!this.form.id) {

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