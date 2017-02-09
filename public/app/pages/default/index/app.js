import {
  Vue,
} from "../../../assets/js/util.js"


import 'element-ui/lib/theme-default/index.css'
import App from './app.vue'

import Barn from '../../barn/index/app.vue'
import Model from '../../model/index/app.vue'


import VueRouter from 'vue-router'

const router = new VueRouter({
  mode: 'hash',
  base: __dirname,
  routes: [{
      path: '/',
      component: Model
    },
    {
      path: '/barn',
      component: Barn,
      children: [{
        path: ':id',
        component: Barn
      }]
    },
    
  ]
})

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})