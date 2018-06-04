import * as types from './mutation-types'
import { setStore, removeStore } from 'common/js/utils'

const mutations = {
  [types.SET_SINGER](state, singer) {
    state.singer = singer
  },
  [types.SET_BOOK](state, book) {
    state.book = book
    setStore('book', state.book)
  },
  [types.SET_READ_MODE](state, mode) {
    state.mode = mode
    setStore('mode', state.mode)
  },
  [types.LOGIN](state, token) {
    state.token = token
    setStore('token', state.token)
  },
  [types.LOGOUT](state) {
    state.token = null
    removeStore('token')
  },
  [types.SET_USER](state, user) {
    state.user = user
    setStore('user', state.user)
  }
}

export default mutations
