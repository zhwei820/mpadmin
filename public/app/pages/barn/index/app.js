import {
  Vue,
} from "../../../assets/js/util.js"


import 'element-ui/lib/theme-default/index.css'
import App from './app.vue'

import ItemEdit from '../item_edit.vue'


import VueRouter from 'vue-router'

const router = new VueRouter({
  mode: 'hash',
  base: __dirname,
  routes: [{
      path: '/',
      component: ItemEdit
    },
    {
      path: '/item_edit',
      component: ItemEdit,
      children: [{
        path: ':id',
        component: ItemEdit
      }]
    },
    
  ]
})

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})