import { getStore } from 'common/js/utils'

export const singer = state => state.singer

export const book = state => state.book.id ? state.book : JSON.parse(getStore('book'))

export const mode = state => state.mode ? state.mode : JSON.parse(getStore('mode'))

export const token = state => state.token ? state.token : getStore('token')