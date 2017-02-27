// import Vue from 'vue'
// import ElementUI from 'element-ui'
// Vue.use(ElementUI)

import {
  Vue
} from "../../../assets/js/util.js"

import '../../../assets/theme/index.css'
import "../../../assets/css/normalize.css"
import App from './app.vue'




new Vue({
  el: '#app',
  render: h => h(App)
})