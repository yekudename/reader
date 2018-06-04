export const commonParams = {
  g_tk: 5381,
  inCharset: 'utf-8',
  outCharset: 'utf-8',
  notice: 0,
  format: 'jsonp'
}

export const options = {
  param: 'jsonpCallback'
}

export const ERR_OK = 0

let baseUrl = ''
let routerMode = 'hash'
let imgBaseUrl = ''

if (process.env.NODE_ENV === 'development') {
  imgBaseUrl = 'http://localhost:8080'
} else if (process.env.NODE_ENV === 'production') {
  baseUrl = 'http://127.0.0.1:5000'
  imgBaseUrl = 'http://127.0.0.1:5000/img/'
}

export {
  baseUrl,
  routerMode,
  imgBaseUrl
}