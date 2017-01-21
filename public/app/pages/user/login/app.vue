<template>
  <div id="app">
    <div class="d">
      登录页
    </div>
    <img v-bind:src="logoImg">
    <h1>{{ msg }}</h1>

<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
  <el-form-item label="Activity name" prop="name">
    <el-input v-model="ruleForm.name"></el-input>
  </el-form-item>
  <el-form-item label="Activity zone" prop="region">
    <el-select v-model="ruleForm.region" placeholder="Activity zone">
      <el-option label="Zone one" value="shanghai"></el-option>
      <el-option label="Zone two" value="beijing"></el-option>
    </el-select>
  </el-form-item>

  <el-form-item>
    <el-button type="primary" @click="handleSubmit">Create</el-button>
    <el-button @click="handleReset">Reset</el-button>
  </el-form-item>
</el-form>
    <el-button @click.native="login">Let's do it</el-button>
  </div>
</template>

<script>
import logo from 'assets/img/logo.png'
export default {
  data () {
    return {
      msg: 'Use Vue 2.0 Today!',
      logoImg: logo,
      
      ruleForm:{
        username:"",
        password:"",
      }
    }
  },

  methods: {
    startHacking () {
      this.$notify({
        title: 'It Works',
        message: 'We have laid the groundwork for you. Now it\'s your time to build something epic!',
        duration: 6000
      })
    },

     make_base_auth(user, password) {
      var tok = user + ':' + password;
      var hash = Base64.encode(tok);
      return "Basic " + hash;
    },
    login() {
      localStorage.setItem("Authorization", this.make_base_auth(this.ruleForm.username, this.ruleForm.password))

      this.$http.get("/api/layers/?" + query).then((response) => {
        debugger
        if (response.status !== 200) {
          this.$message({
            type: 'info',
            message: '请求失败, 请重试'
          });
        }
      }, (response) => {
        this.$message({
          type: 'info',
          message: '请求失败, 请重试'
        });
      });
    },
    

  }
}
</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}
</style>
