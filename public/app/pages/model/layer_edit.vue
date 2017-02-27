<template>
  <!--<el-dialog title="CI模型层编辑" v-model="dialogFormVisible">-->
  <el-row type="flex" class="row-bg" justify="center">
    <el-col :span="6">
      <h2><span v-if="layerId_1">编辑</span><span v-else>新建</span>CI模型层</h2>
      <el-form :model="form" label-position="top">
        <el-form-item label="CI模型层名称" label-width="80">
          <el-input v-model="form.name" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div>
        <el-row type="flex" class="row-bg" justify="end">
          <el-col :span="24">
            <el-button size="mini" type="danger" @click="deleteLayer()" :class="{'hidden': !this.form.id || this.form.name == 'default'}">删除</el-button>
          </el-col>
          <el-button type="primary" @click="submit">确 定</el-button>
        </el-row>
      </div>
    </el-col>
  </el-row>
  <!--</el-dialog>-->
</template>
<script>
  import {
    excel,
    deepCopyOfObject,
    paramParse

  } from "../../assets/js/util.js"

  export default {
    data() {
      return {
        layerId_1: "",
        input2: "",
        form: {
          name: '',
          id: "",
        },
        _form: {},
        id: 0,
      }
    },
    props: ['layerId'],
    watch: {
      layerId: function (dest, src) {
        this.layerId_1 = this.layerId
        this.fetch(0, 100)
      }
    },

    beforeMount: function () {
      window.vm_m_n = this;
      this._form = deepCopyOfObject(this.form)
      this.layerId_1 = this.layerId

      this.fetch(0, 100)
    },
    methods: {
      fetch(offset, limit) {
        // var id = this.$route.params.id
        // this.id = id == undefined ? 0 : id

        if (this.layerId_1) {
          this.$http.get("/api/layers/" + this.layerId_1 + "/?" + Date.now()).then((response) => {
            this.form = response.data

          }, (response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });
        } else {
          this.form = deepCopyOfObject(this._form)
        }
      },
      submit() {
        if (!this.form.id) {
          this.$http.post("/api/layers/", this.form).then((response) => {
            window.vm_m.get_model_menus()
            // this.$router.push({
            //   path: "/layer_edit/" + response.data.id
            // })
            this.layerId_1 = response.data.id
            this.fetch(0, 100)
            parent.vm.show_ok_message("新建成功！")

          }, (
            response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });

        } else {
          this.$http.put("/api/layers/" + this.form.id + "/", this.form).then((response) => {
            console.log(this.form);
            window.vm_m.get_model_menus()
            parent.vm.show_ok_message("编辑成功！")

          }, (
            response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });

        }
      },
      deleteLayer() {
        if (this.form.id) {
          this.$http.delete("/api/layers/" + this.form.id + "/").then((response) => {
            window.vm_m.get_model_menus()
            this.layerId_1 = ""
            parent.vm.show_ok_message("删除成功！")

          }, (response) => {
            parent.vm.show_error_message(response.data.error)
          });
        }

      },
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
  
  .right_export {
    float: right;
  }
</style>