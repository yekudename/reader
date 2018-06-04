<template>
  <div class="singer" ref="singer">
    <index-list :data="singers">
      <index-list-group v-for="(group, index) in singers" :key="index" :group="group">
        <index-list-item class="item" v-for="(item, index) in group.items" :key="index" :item="item" @select="selectSinger">
          <img class="avatar" v-lazy="item.avatar">
          <span class="name">{{item.name}}</span>
        </index-list-item>
      </index-list-group>
    </index-list>
    <router-view></router-view>
  </div>
</template>

<script>
import {getSingerList, getSingerListByLocal} from 'api/singer'
import {ERR_OK} from 'api/config'
import Singer from 'common/js/singer'
import IndexList from 'base/index-list/index-list'
import IndexListGroup from 'base/index-list/index-list-group'
import IndexListItem from 'base/index-list/index-list-item'
import {mapMutations} from 'vuex'

const HOT_NAME = '热门'
const HOT_SINGER_LENGTH = 10

export default {
  data() {
    return {
      singers: []
    }
  },
  created() {
    this._getSingerListByLocal()
  },
  methods: {
    selectSinger(singer) {
      this.$router.push({
        path: `/singer/${singer.id}`
      })
      this.setSinger(singer)
    },
    _getSingerList() {
      getSingerList().then((res) => {
        if (res.code === ERR_OK) {
          this.singers = this._nomalizeSinger(res.data)
          console.log(this.singers)
        }
      })
    },
    _getSingerListByLocal() {
      getSingerListByLocal().then((res) => {
        if (res.errno === ERR_OK) {
          this.singers = res.data
        }
      })
    },
    _nomalizeSinger(list) {
      let map = {
        hot: {
          title: HOT_NAME,
          items: []
        }
      }
      list.forEach((item, index) => {
        if (index < HOT_SINGER_LENGTH) {
          map.hot.items.push(new Singer({
            name: item.Fsinger_name,
            id: item.Fsinger_mid
          }))
        }
        const key = item.Findex
        if (!map[key]) {
          map[key] = {
            title: key,
            items: []
          }
        }
        map[key].items.push(new Singer({
          name: item.Fsinger_name,
          id: item.Fsinger_mid
        }))
      })

      let hot = []
      let ret = []
      for (var k in map) {
        let val = map[k]
        if (val.title.match(/[a-zA-Z]/)) {
          ret.push(val)
        } else if (val.title === HOT_NAME) {
          hot.push(val)
        }
      }
      ret.sort((a, b) => {
        return a.title.charCodeAt(0) - b.title.charCodeAt(0)
      })
      return hot.concat(ret)
    },
    ...mapMutations({
      setSinger: 'SET_SINGER'
    })
  },
  components: {
    IndexList,
    IndexListGroup,
    IndexListItem
  }

}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @require '~common/stylus/variable.styl'
  .singer
    position: fixed
    top: 88px
    bottom: 0
    width: 100%
    .item
      display: flex
      align-items: center
      padding: 20px 0 0 30px
      .avatar
        width: 50px
        height: 50px
        border-radius: 50%
      .name
        margin-left: 20px
        color: $color-grey
        font-size: $fontsize-medium
</style>
