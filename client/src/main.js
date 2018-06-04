import 'babel-polyfill'
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import fastclick from 'fastclick'
import LazyLoad from 'vue-lazyload'
import FontAwesome from 'font-awesome/css/font-awesome.css'

import 'common/stylus/index.styl'

fastclick.attach(document.body)

Vue.use(LazyLoad, {
  loading: require('common/image/default.png')
})
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  FontAwesome,
  render: h => h(App)
})
