import fetch from './fetch'

/**
 * 获取food页面的 category 种类列表
 */

export const bookCategory = () => fetch('/api/category')

export const rankBookList = (rankid, offset = '20') => {
  let data = {
    rankid,
    offset
  }
  return fetch('/api/rankBookList', data)
}

/**
 * @param {电话号码} phone
 * @param {密码} password
 */
export const register = (nickname, password) => fetch('/api/user', {nickname, password}, 'POST')

export const bookList = () => fetch('/api/novel')

export const book = id => fetch('/api/novel/' + id)

export const chapter = id => fetch('/api/chapter/' + id)

export const chapterDetail = id => fetch('/api/chapter_detail/' + id)

export const userList = () => fetch('/api/user')

export const user = id => fetch('/api/user/' + id)

export const search = (query, page, perpage) => fetch('/api/search', {query, page, perpage})