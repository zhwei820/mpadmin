<template>
  <div>
    <!--<el-menu theme="dark" default-active="1" class="el-menu-demo" mode="horizontal">
      <el-menu-item index="1">CMDB管理中心</el-menu-item>
    </el-menu>-->
    <el-row class="tac">
      <el-col :span="4">
        <el-menu class="el-menu-vertical-demo" @select="handleSelect" @open="handleOpen">
          <div>
            <el-button size="large" type="primary" class="new_btn" @click="createNewLayer()">
              <i class="fa fa-plus"></i> 新增CI模型层
            </el-button>
          </div>
          <div>
            <el-button size="large" type="primary" class="new_btn" @click="createNewGroup()">
              <i class="fa fa-plus"></i> 新增CI模型组
            </el-button>
          </div>
          <div>
            <el-button size="large" type="primary" class="new_btn" @click="createNewItemCategory()">
              <i class="fa fa-plus"></i> 新增CI模型
            </el-button>
          </div>
          <el-submenu :index="submenus.uri" v-for="submenus in menus">
            <template slot="title"><i class="el-icon-message"></i>{{submenus.text}}</template>
            <!--<el-menu-item :index="submenu.uri" v-for="submenu in submenus.items">{{submenu.text}}</el-menu-item>-->
            <el-submenu :index="submenus1.uri" v-for="submenus1 in submenus.menus">
              <template slot="title"><i class="el-icon-message"></i>{{submenus1.text}}</template>
              <el-menu-item :index="submenu.uri" v-for="submenu in submenus1.items">{{submenu.text}}</el-menu-item>
            </el-submenu>
          </el-submenu>
        </el-menu>
      </el-col>
      <!--sidebar end-->
      <el-col :span=20>
        <el-breadcrumb separator="/" class="breadcrumb_padding">
          <!--<el-breadcrumb-item>首页</el-breadcrumb-item>
          <el-breadcrumb-item>{{breadcrumb1}}</el-breadcrumb-item>
          <el-breadcrumb-item>{{breadcrumb2}}</el-breadcrumb-item>-->
        </el-breadcrumb>
        <iframe id="checkListFrame" src="/model/layer_edit.html" frameborder="0" width="100%" height="90%" scrolling="auto"></iframe>
      </el-col>
    </el-row>
    <div id="footer">
      <hr>
      <footer class="text-center">
        <p>© 我的公司</p>
      </footer>
    </div>
  </div>
</template>
<script>
  import {
    addEvent
  } from "../../../assets/js/util.js"

  export default {
    data() {
      return {
        breadcrumb1: "dashboard",
        breadcrumb2: "",
        menus: [],

        // menus: [{
        //   uri: "/",
        //   text: "层",
        //   menus: [{
        //     uri: "/model/layer.html?123",
        //     text: "组",
        //     items: [{
        //       text: "模型",
        //       uri: "/model/layer.html?123",
        //     }, {
        //       text: "模型",
        //       uri: "/model/group.html?1233",
        //     }, {
        //       text: "模型",
        //       uri: "/model/item_category.html?1232",
        //     }, ]
        //   }, {
        //     uri: "/model/group.html?123",
        //     text: "组",
        //     items: [{
        //       text: "模型",
        //       uri: "/model/layer.html?1213",
        //     }, {
        //       text: "模型",
        //       uri: "/model/group.html?12313",
        //     }, {
        //       text: "模型",
        //       uri: "/model/item_category.html?12132",
        //     }, ]
        //   }],
        // }],
        menus1: {},
      }
    },
    mounted: function () {
      this.get_model_menus()
      window.vm = this;
    },
    methods: {
      get_model_menus() {
        var that = this
        var layer_list, layer_name_list
        var p1 = new Promise(
          function (resolve, reject) {
            that.get_model_data("/api/layers/", "", resolve, reject)
          }
        );

        var group_list, group_name_list, group_by_list_of_group
        var p2 = new Promise(
          function (resolve, reject) {
            that.get_model_data("/api/groups/", "layer", resolve, reject)
          }
        );


        var item_category_list, item_category_name_list, group_by_list_of_item_category
        var p3 = new Promise(
          function (resolve, reject) {
            that.get_model_data("/api/items_categories/", "group", resolve, reject)
          }
        );


        p1.then((res) => {
          layer_list = res[0];
          layer_name_list = res[1]
          // console.log(layer_name_list)
          return p2 // 黑科技!
        }).then((res) => {
          group_list = res[0];
          group_name_list = res[1]
          group_by_list_of_group = res[2]

          // console.log(group_name_list)
          return p3
        }).then((res) => {
          item_category_list = res[0];
          item_category_name_list = res[1]
          group_by_list_of_item_category = res[2]

          // console.log(item_category_name_list)

          this.menus = []

          for (var key in layer_name_list) {
            var element = layer_name_list[key];
            var m1 = {
              uri: "/model/layer_edit.html?id=" + key,
              text: element,
              items: []
            }
            var menus1 = []

            for (var key1 in group_by_list_of_group[key]) {
              var element1 = group_by_list_of_group[key][key1];

              var menus2 = {};
              menus2.uri = "/model/group_edit.html?id=" + element1.id
              menus2.text = element1.name
              menus2.items = []
              for (var key2 in group_by_list_of_item_category[element1.id]) {
                var element2 = group_by_list_of_item_category[element1.id][key2];
                var menu_item = {}
                menu_item.uri = "/model/item_category_edit.html?id=" + element2.id
                menu_item.text = element2.name
                menus2.items.push(menu_item)
              }
              menus1.push(menus2)
            }
            m1.menus = menus1;

            this.menus.push(m1)
          }

          // for (var ii = 0; ii < this.menus.length; ii++) {
          //   this.menus1[this.menus[ii].uri] = {}
          //   this.menus1[this.menus[ii].uri]['text'] = this.menus[ii]['text']


          //   for (var jj = 0; jj < this.menus[ii].items.length; jj++) {
          //     this.menus1[this.menus[ii].uri][this.menus[ii].items[jj]['uri']] =
          //       this.menus[ii].items[jj]
          //   }
          // }

          // var breadcrumb1 = document.getElementsByClassName("el-breadcrumb__item")[0]

          // function breadcrumb_home() {
          //   location.href = "/model/index.html"
          // }
          // addEvent(breadcrumb1, "click", breadcrumb_home)

        })

      },
      get_model_data(url, group_by, resolve, reject) {
        var query = ""
        var list, name_list, group_by_list
        this.$http.get(url + query).then((response) => {
          if (response.status !== 200) {
            this.$message({
              type: 'info',
              message: '请求失败, 请重试'
            });
          }
          list = {}
          for (var key in response.data) {
            list[response.data[key].name] = response.data[key].id;
          }
          name_list = {}
          for (var key in response.data) {
            name_list[response.data[key].id] = response.data[key].name;
          }

          group_by_list = {}
          if (group_by) {
            for (var key in response.data) {
              if (group_by_list[response.data[key][group_by]] == undefined) {
                group_by_list[response.data[key][group_by]] = []
              }
              group_by_list[response.data[key][group_by]].push(response.data[key]);
            }
          }
          resolve([list, name_list, group_by_list])
        }, (response) => {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
          reject()
        });
      },
      handleSelect(key, keyPath) {
        document.getElementById("checkListFrame").src = key
        // this.breadcrumb1 = this.menus1[keyPath[0]]['text']
        // this.breadcrumb2 = this.menus1[keyPath[0]][keyPath[1]]['text']
      },
      handleOpen(key, keyPath) {

        if (key != "/") {
          document.getElementById("checkListFrame").src = key
          // console.log(this.menus1);

          // this.breadcrumb1 = this.menus1[keyPath[0]]['text']
          // this.breadcrumb2 = this.menus1[keyPath[0]][keyPath[1]]['text']
        }
      },
      createNewLayer() {
        document.getElementById("checkListFrame").src = "/model/layer_edit.html?id="
      },
      createNewGroup() {
        document.getElementById("checkListFrame").src = "/model/group_edit.html?id="
      },
      createNewItemCategory() {
        document.getElementById("checkListFrame").src = "/model/item_category_edit.html?id="
      },
    }
  }


  function dyniframesize() {
    var iframe = document.getElementById("checkListFrame");
    try {
      var bHeight = iframe.contentWindow.document.body.scrollHeight;
      var dHeight = iframe.contentWindow.document.documentElement.scrollHeight;

      var bHeight = document.body.scrollHeight;
      var dHeight = document.documentElement.scrollHeight;

      var height = Math.max(bHeight, dHeight);
      iframe.height = height;
    } catch (ex) {}
  }
  if (window.addEventListener) window.addEventListener("load", dyniframesize, false)
  else if (window.attachEvent) window.attachEvent("onload", dyniframesize)
  else window.onload = dyniframesize
</script>
<style scoped>
  @import '../../../assets/css/normalize.css';
  @import '../../../assets/css/index.css';
  body {
    font-family: Helvetica, sans-serif;
  }
  
  .new_btn {
    margin-left: -70px;
    left: 50%;
    position: relative;
    margin-bottom: 3px;
  }
</style>