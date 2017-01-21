<template>
  <div id="app">
    <div class="d">
      登录页
    </div>
    <img v-bind:src="logoImg">
    <h1>{{ msg }}</h1>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
      <el-form-item label="username" prop="username">
        <el-input v-model="ruleForm.username"></el-input>
      </el-form-item>
      <el-form-item label="password" prop="password">
        <el-input v-model="ruleForm.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="login">Create</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import logo from 'assets/img/logo.png'
  export default {
    data() {
      return {
        msg: 'Use Vue 2.0 Today!',
        logoImg: logo,

        ruleForm: {
          username: "",
          password: "",
        },
        rules: {
          name: [{
              required: true,
              message: 'Please input Activity name',
              trigger: 'blur'
            },
            {
              min: 3,
              max: 5,
              message: 'Length should be 3 to 5',
              trigger: 'blur'
            }
          ],
          region: [{
            required: true,
            message: 'Please select Activity zone',
            trigger: 'change'
          }],
          date1: [{
            type: 'date',
            required: true,
            message: 'Please pick a date',
            trigger: 'change'
          }],
          date2: [{
            type: 'date',
            required: true,
            message: 'Please pick a time',
            trigger: 'change'
          }],
          type: [{
            type: 'array',
            required: true,
            message: 'Please select at least one activity type',
            trigger: 'change'
          }],
          resource: [{
            required: true,
            message: 'Please select activity resource',
            trigger: 'change'
          }],
          desc: [{
            required: true,
            message: 'Please input activity form',
            trigger: 'blur'
          }]
        }
      }
    },

    methods: {
      startHacking() {
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