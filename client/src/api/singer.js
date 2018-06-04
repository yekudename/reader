import jsonp from 'common/js/jsonp'
import {commonParams, options} from './config'
import axios from 'axios'

export function getSingerList() {
  const url = 'http://c.y.qq.com/v8/fcg-bin/v8.fcg'

  const data = Object.assign({}, commonParams, {
    channel: 'singer',
    page: 'list',
    key: 'all_all_all',
    pagesize: 100,
    pagenum: 1,
    hostUin: 0,
    needNewCode: 0,
    platfoem: 'yqq',
    g_tk: 1664029744
  })

  return jsonp(url, data, options)
}

export function getSingerListByLocal() {
  const url = '/api/getSingerList'
  return axios.get(url).then((res) => {
    return Promise.resolve(res.data)
  })
}
