<template>
  <div>
    <el-menu theme="dark" default-active="1" class="el-menu-demo" mode="horizontal">
      <el-menu-item index="1">处理中心</el-menu-item>
      <el-submenu index="2">
        <template slot="title">我的工作台</template>
        <el-menu-item index="2-1">选项1</el-menu-item>
        <el-menu-item index="2-2">选项2</el-menu-item>
        <el-menu-item index="2-3">选项3</el-menu-item>
      </el-submenu>
      <el-menu-item index="3">订单管理</el-menu-item>
    </el-menu>
    <el-row class="tac">
      <!--sidebar start-->
      <el-col :span="4">
        <!--<h5>菜单</h5>-->
        <el-menu class="el-menu-vertical-demo" @select="handleSelect" @open="handleOpen" unique-opened="true">
          <el-submenu :index="submenus.id" v-for="submenus in menus">
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
        <iframe id="checkListFrame" src="/user/table.html" frameborder="0" width="100%" height="90%" scrolling="auto"></iframe>
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
  // console.log(addEvent)

  export default {
    data() {
      return {
        breadcrumb1: "dashboard",
        breadcrumb2: "",

        menus: [{
          id: "1",
          text: "导航1",
          items: [{
            text: "tooltip",
            uri: "/user/tooltip.html?123",
          }, {
            text: "表单2",
            uri: "/user/form.html?1233",
          }, {
            text: "表格1",
            uri: "/user/table.html?1232",
          }, ]
        }, {
          id: "2",
          text: "导航2",
          items: [{
            text: "tooltip",
            uri: "/user/tooltip.html?123f",
          }, {
            text: "表单2",
            uri: "/user/form.html?123d",
          }, {
            text: "表格1",
            uri: "/user/table.html?123g",
          }, ]
        }, {
          id: "3",
          text: "导航3",
          items: [{
            text: "card",
            uri: "/user/card.html?12332",
          }, {
            text: "表单2",
            uri: "/user/form.html?123fg",
          }, {
            text: "表格1",
            uri: "/user/table.html?123dds",
          }, ]
        }, ],
        menus1: {},
      }
    },
    mounted: function () {
      for (var ii = 0; ii < this.menus.length; ii++) {
        this.menus1[this.menus[ii].id] = {}
        this.menus1[this.menus[ii].id]['text'] = this.menus[ii]['text']
        for (var jj = 0; jj < this.menus[ii].items.length; jj++) {
          this.menus1[this.menus[ii].id][this.menus[ii].items[jj]['uri']] = this.menus[ii].items[jj]
        }
      }


      var breadcrumb1 = document.getElementsByClassName("el-breadcrumb__item")[0]

      function breadcrumb_home() {
        location.href = "/user/index.html"
      }
      addEvent(breadcrumb1, "click", breadcrumb_home)

    },
    methods: {
      handleSelect(key, keyPath) {
        document.getElementById("checkListFrame").src = key
        this.breadcrumb1 = this.menus1[keyPath[0]]['text']
        this.breadcrumb2 = this.menus1[keyPath[0]][keyPath[1]]['text']
      },
      handleOpen(key, keyPath) {
        // debugger
        // $(".el-submenu").removeClass("is-opened")
        // $("ul[class='el-menu']").css('display','none'); 
      },

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
</style>