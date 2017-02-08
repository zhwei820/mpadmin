import {
  Vue,
} from "../../../assets/js/util.js"


import 'element-ui/lib/theme-default/index.css'
import App from './app.vue'

import Items from '../items.vue'


import VueRouter from 'vue-router'

const router = new VueRouter({
  mode: 'hash',
  base: __dirname,
  routes: [{
      path: '/',
      component: Items
    },
    {
      path: '/items',
      component: Items,
      children: [{
        path: ':id',
        component: Items
      }]
    },
    
  ]
})

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})