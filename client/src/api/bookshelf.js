import axios from 'axios'

export function getBookshelf() {
  const url = '/api/getBookshelf'
  return axios.get(url).then((res) => {
    return Promise.resolve(res.data)
  })
}

export function getBooksGroup() {
  const url = '/api/getBooksGroup'
  return axios.get(url).then((res) => {
    return Promise.resolve(res.data)
  })
}
