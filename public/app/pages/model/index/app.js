import {
  Vue,
} from "../../../assets/js/util.js"


import 'element-ui/lib/theme-default/index.css'
import App from './app.vue'

import LayerEdit from '../layer_edit.vue'
import GroupEdit from '../group_edit.vue'
import ItemCategoryEdit from '../item_category_edit.vue'

import VueRouter from 'vue-router'

const About = {
  template: '<div><h2>About</h2></div>'
}

const router = new VueRouter({
  mode: 'hash',
  base: __dirname,
  routes: [{
      path: '/',
      component: LayerEdit
    },
    {
      path: '/layer_edit',
      component: LayerEdit,
      children: [{
        path: ':id',
        component: LayerEdit
      }]
    },
    {
      path: '/group_edit',
      component: GroupEdit,
      children: [{
        path: ':id',
        component: GroupEdit
      }]
    },
    {
      path: '/item_category_edit',
      component: ItemCategoryEdit,
      children: [{
        path: ':id',
        component: ItemCategoryEdit
      }],
    },
  ]
})

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})