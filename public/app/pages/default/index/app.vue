<template>
  <div class="" class="height_100">
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
    <el-row class="tac height_100" :gutter="20">
      <el-col :span="4">
        <el-menu mode="vertical" default-active="1" class="el-menu-vertical-demo" @select="handleSelect">
          <!--<el-menu-item-group title="分组一">
            <el-menu-item index="1"><i class="el-icon-message"></i>导航一</el-menu-item>
            <el-menu-item index="2"><i class="el-icon-message"></i>导航二</el-menu-item>
          </el-menu-item-group>-->
          <!--<el-menu-item-group title="分组二">-->
            <el-menu-item index="/model/index.html"><i class="fa fa-cogs"></i> 模型</el-menu-item>
            <el-menu-item index="/model/index.html?"><i class="fa fa-cogs"></i> 模型</el-menu-item>
          <!--</el-menu-item-group>-->
        </el-menu>
      </el-col>
      <el-col :span=20 class="height_100">
        <el-breadcrumb separator="/" class="breadcrumb_padding">
          <el-breadcrumb-item>首页</el-breadcrumb-item>
          <el-breadcrumb-item>{{breadcrumb1}}</el-breadcrumb-item>
          <el-breadcrumb-item>{{breadcrumb2}}</el-breadcrumb-item>
        </el-breadcrumb>
        <iframe id="checkListFrame1" class="height_100" src="/model/index.html" frameborder="0" width="100%" height="90%" scrolling="auto"></iframe>
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
  export default {
    data() {
      return {
        breadcrumb1: "dashboard",
        breadcrumb2: "",

        menus1: {},
      }
    },
    mounted: function () {
      console.log(this.menus);

      // for (var ii = 0; ii < this.menus.length; ii++) {
      //   this.menus1[this.menus[ii].id] = {}
      //   this.menus1[this.menus[ii].id]['text'] = this.menus[ii]['text']
      //   for (var jj = 0; jj < this.menus[ii].items.length; jj++) {
      //     this.menus1[this.menus[ii].id][this.menus[ii].items[jj]['uri']] = this.menus[ii].items[jj]
      //   }
      // }

    },
    methods: {
      handleSelect(key, keyPath) {
        document.getElementById("checkListFrame1").src = key
        // this.breadcrumb1 = this.menus1[keyPath[0]]['text']
        // this.breadcrumb2 = this.menus1[keyPath[0]][keyPath[1]]['text']
      },
      handleOpen(key, keyPath) {},
    }
  }

  // function dyniframesize() {
  //   var iframe = document.getElementById("checkListFrame1");
  //   try {
  //     var bHeight = iframe.contentWindow.document.body.scrollHeight;
  //     var dHeight = iframe.contentWindow.document.documentElement.scrollHeight;

  //     var bHeight = document.body.scrollHeight;
  //     var dHeight = document.documentElement.scrollHeight;

  //     var height = Math.max(bHeight, dHeight);
  //     iframe.height = height;
  //   } catch (ex) {}
  // }
  // if (window.addEventListener) window.addEventListener("load", dyniframesize, false)
  // else if (window.attachEvent) window.attachEvent("onload", dyniframesize)
  // else window.onload = dyniframesize
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
  
  .edit_mini_btn {
    background: transparent;
    border: navajowhite;
  }

</style>