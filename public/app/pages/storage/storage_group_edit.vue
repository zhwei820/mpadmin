<template>
  <div>
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="6">
        <h2><span v-if="id">编辑</span><span v-else>新建</span>管理项目</h2>
        <el-form label-position="top">
          <el-form-item label="管理项目名称">
            <el-input v-model="form.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="父管理项目">
            <el-select v-model="form.group" placeholder="请选择">
              <el-option v-bind:label="item" v-bind:value="index" v-for="(item, index) in storageGroupListExceptOwnGroup">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <div class="dialog-footer">
          <el-row type="flex" class="row-bg" justify="end">
            <el-col :span="24">
              <el-button size="mini" type="danger" @click="deleteGroup()" :class="{'hidden': !this.form.id || this.form.name == 'default'}">删除</el-button>
            </el-col>
            <el-button type="primary" @click="submit">确 定</el-button>
          </el-row>
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

  } from "../../assets/js/util.js"

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
        _form: {},
        layer_list: {},
        layer_name_list: {},
        formLabelWidth: '120px',
        id: 0,
        storageGroupListExceptOwnGroup: {},
        filter_ids: [],
      }
    },
    props: ['groupId', 'storageGroupList', 'nestedList'],
    watch: {
      groupId: function (dest, src) {
        this.fetch(0, 100)
      },
      storageGroupList: function (dest, src) {
        this.fetch(0, 100)
      }
    },
    mounted: function () {
      this._form = deepCopyOfObject(this.form)
      this.fetch(0, 100)
      window.vm_m_n = this;
    },
    methods: {
      recursive_filter(children, id) { // 过滤本组id
        for (var key in children) {
          var element = children[key];
          if (element.id == id) {
            this.filter_ids.push(id)
            this.recursive_get_ids(element.children)
          } else {
            this.recursive_filter(element.children, id)
          }
        }
      },
      recursive_get_ids(children) {
        for (var key in children) {
          var element = children[key];
          this.filter_ids.push(element.id)
          this.recursive_get_ids(element.children)
        }
      },
      fetch(offset, limit) {
        // var id = paramParse('id')
        // var id = this.$route.params.id
        // this.id = id == undefined ? 0 : id
        this.filter_ids = []
        console.log(this.groupId);
        var tmp = deepCopyOfObject(this.storageGroupList)
        this.storageGroupListExceptOwnGroup = tmp
        this.recursive_filter(this.nestedList, this.groupId)
        // console.log(this.filter_ids);
        for (var ii = 0; ii < this.filter_ids.length; ii++) {
          delete this.storageGroupListExceptOwnGroup[this.filter_ids[ii]]
        }

        if (this.groupId) {
          this.$http.get("/api/storage_groups/" + this.groupId + "/?t=" + Date.now()).then((response) => {
            this.form = response.data
          }, (response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });
        } else {
          var form = deepCopyOfObject(this._form)
          form.group = ''
          this.form = form
        }
      },
      submit() {
        if (!this.form.id) {
          this.$http.post("/api/storage_groups/", this.form).then((response) => {
            window.vm_m.get_model_menus()
            // this.$router.push({
            //   path: "/group_edit/" + response.data.id
            // })
          }, (
            response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });

        } else {
          this.$http.put("/api/storage_groups/" + this.form.id + "/", this.form).then((response) => {
            window.vm_m.get_model_menus()
            // this.$router.push({
            //   path: "/group_edit/" + response.data.id
            // })
          }, (
            response) => {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          });
        }
      },
      deleteGroup() {
        if (this.form.id) {
          this.$http.delete("/api/storage_groups/" + this.form.id + "/").then((response) => {
            window.vm_m.id = ""
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