import axios from 'axios'
import store from '../store/index'
import router from '../router/index'
import * as types from '../store/mutation-types'
import { baseUrl } from './config'

axios.defaults.timeout = 5000
axios.defaults.baseURL = baseUrl

axios.interceptors.request.use(
  config => {
    if (store.getters.token) {
      config.headers.Authorization = `JWT ${store.getters.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          store.commit(types.LOGOUT)
          router.replace({
            path: '/login',
            query: {redirect: router.currentRoute.fullPath}
          })
      }
    }
    return Promise.reject(error.response.data)
  }
)

export default axios