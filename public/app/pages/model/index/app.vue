<template>
  <div>
    <!--<el-menu theme="dark" default-active="1" class="el-menu-demo" mode="horizontal">
      <el-menu-item index="1">CMDB管理中心</el-menu-item>
    </el-menu>-->
    <el-row class="tac">
      <!--sidebar start-->
      <el-col :span="4">
        <el-menu class="el-menu-vertical-demo" @select="handleSelect" @open="handleOpen" unique-opened=true>
          <div>
            <el-button size="large" type="primary" class="new_btn" @click="createNewLayer()">
              <i class="fa fa-plus"></i> 新增CI模型层
            </el-button>
          </div>
          <div>
            <el-button size="large" type="primary" class="new_btn" @click="createNewLayer()">
              <i class="fa fa-plus"></i> 新增CI模型组
            </el-button>
          </div>
          <div>
            <el-button size="large" type="primary" class="new_btn" @click="createNewLayer()">
              <i class="fa fa-plus"></i> 新增CI模型
            </el-button>
          </div>
          <el-submenu :index="submenus.uri" v-for="submenus in menus">
            <template slot="title"><i class="el-icon-message"></i>{{submenus.text}}</template>
            <el-menu-item :index="submenu.uri" v-for="submenu in submenus.items">{{submenu.text}}</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-col>
      <!--sidebar end-->
      <el-col :span=20>
        <el-breadcrumb separator="/" class="breadcrumb_padding">
          <el-breadcrumb-item>首页</el-breadcrumb-item>
          <el-breadcrumb-item>{{breadcrumb1}}</el-breadcrumb-item>
          <el-breadcrumb-item>{{breadcrumb2}}</el-breadcrumb-item>
        </el-breadcrumb>
        <iframe id="checkListFrame" src="/model/layer.html" frameborder="0" width="100%" height="90%" scrolling="auto"></iframe>
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

        // menus: [{
        //   uri: "/",
        //   text: "模型",
        menus: [{
          uri: "/model/layer.html?123",
          text: "导航1",
          items: [{
            text: "layer",
            uri: "/model/layer.html?123",
          }, {
            text: "group",
            uri: "/model/group.html?1233",
          }, {
            text: "CIModel",
            uri: "/model/item_category.html?1232",
          }, ]
        }, {
          uri: "/model/group.html?123",
          text: "导航2",
          items: [{
            text: "layer",
            uri: "/model/layer.html?1213",
          }, {
            text: "group",
            uri: "/model/group.html?12313",
          }, {
            text: "CIModel",
            uri: "/model/item_category.html?12132",
          }, ]
        }, {
          uri: "/model/item_category.html?123",
          text: "导航3",
          items: [{
            text: "layer",
            uri: "/model/layer.html?1233",
          }, {
            text: "group",
            uri: "/model/group.html?12323",
          }, {
            text: "CIModel",
            uri: "/model/item_category.html?12432",
          }, ]
        }, ],
        // }],
        menus1: {},
      }
    },
    mounted: function () {
      var that = this
      var layer_list, layer_name_list
      var p1 = new Promise(
        function (resolve, reject) {
          that.get_model_data("/api/layers/", resolve, reject)
        }
      );

      var group_list, group_name_list
      var p2 = new Promise(
        function (resolve, reject) {
          that.get_model_data("/api/groups/", resolve, reject)
        }
      );


      var item_category_list, item_category_name_list
      var p3 = new Promise(
        function (resolve, reject) {
          that.get_model_data("/api/items_categories/", resolve, reject)
        }
      );


      p1.then((res) => {
        layer_list = res[0];
        layer_name_list = res[1]
        console.log(layer_name_list)
        return p2 // 黑科技!
      }).then((res) => {
        group_list = res[0];
        group_name_list = res[1]
        console.log(group_name_list)
        return p3
      }).then((res) => {
        item_category_list = res[0];
        item_category_name_list = res[1]
        console.log(item_category_name_list)


        for (var ii = 0; ii < this.menus.length; ii++) {
          this.menus1[this.menus[ii].uri] = {}
          this.menus1[this.menus[ii].uri]['text'] = this.menus[ii]['text']

          for (var jj = 0; jj < this.menus[ii].items.length; jj++) {
            this.menus1[this.menus[ii].uri][this.menus[ii].items[jj]['uri']] =
              this.menus[ii].items[jj]
          }
        }

        var breadcrumb1 = document.getElementsByClassName("el-breadcrumb__item")[0]

        function breadcrumb_home() {
          location.href = "/model/index.html"
        }
        addEvent(breadcrumb1, "click", breadcrumb_home)

      })


    },
    methods: {
      get_model_menus() {

      },
      get_model_data(url, resolve, reject) {
        var query = ""
        var list, name_list
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
          resolve([list, name_list])
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
        this.breadcrumb1 = this.menus1[keyPath[0]]['text']
        this.breadcrumb2 = this.menus1[keyPath[0]][keyPath[1]]['text']
      },
      handleOpen(key, keyPath) {

        if (key != "/") {
          document.getElementById("checkListFrame").src = key
          console.log(this.menus1);

          this.breadcrumb1 = this.menus1[keyPath[0]]['text']
          this.breadcrumb2 = this.menus1[keyPath[0]][keyPath[1]]['text']
        }
      },
      createNewLayer() {

      }

    }
  }


  var iframeids = ["checkListFrame"]
  var iframehide = "yes"

  function iFrameHeight() {
    var ifm = document.getElementById("checkListFrame");
    var subWeb = document.frames ? document.frames["iframepage"].document : ifm.contentDocument;

    if (ifm != null && subWeb != null) {
      ifm.height = subWeb.body.scrollHeight;
    }

  }
  if (window.addEventListener) window.addEventListener("load", iFrameHeight, false)
  else if (window.attachEvent) window.attachEvent("onload", iFrameHeight)
  else window.onload = iFrameHeight
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