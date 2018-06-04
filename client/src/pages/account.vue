<template>
  <div class="account">
    <scroll
      ref="scroll"
      :options="options"
      :data="optionItems">
      <div class="login-wrapper" @click="gotoLogin">
        <div class="account-user">
          <i class="fa fa-circle fa-5x"></i>
          <i class="fa fa-user fa-3x"></i>
        </div>
        <div class="title">登陆 / 注册</div>
      </div>
      <div class="option-list-content" ref="content">
        <ul>
          <cell
            class="border-bottom-1px"
            v-for="(item, index) in optionItems"
            :key="index"
            :title="item.title"
            iconRight="angle-right"
            is-link
            @select="selectItem"
            :to="item.to">
          </cell>
        </ul>
      </div>
    </scroll>
  </div>
</template>

<script>
import AButton from 'base/button/a-button'
import ButtonGroup from 'components/button-group/button-group'
import Cell from 'components/cell/cell'
import Scroll from 'base/scroll/scroll'
import apiMixin from 'common/mixins/api'
import axios from 'axios'
import {mapGetters} from 'vuex'

export default {
  name: 'account',
  mixins: [apiMixin],
  components: {
    AButton,
    ButtonGroup,
    Cell,
    Scroll
  },
  data() {
    return {
      optionItems: [
        {
          icon: 'icon-music',
          title: '会员等级',
          to:'/'
        },
        {
          icon: 'icon-music',
          title: '我的等级',
          to:'/'
        },
        {
          icon: 'icon-music',
          title: '我的阅历',
          to:'/'
        },
        {
          icon: 'icon-music',
          title: '我的徽章',
          to:'/'
        }
      ]
    }
  },
  computed: {
    ...mapGetters(['token'])
  },
  created() {
    this.getUser()
  },
  methods: {
    gotoLogin() {
      this.$router.push('/login')
    },
    selectItem(item) {
      console.log(item.title)
    },
    cancel() {
      console.log('cancel')
    },
    confirm() {
      console.log('confirm')
    },
    handlePopup() {
      if (this.isVisible) {
        return
      }

      this.isVisible = true
    },
    getUser() {
      axios.get('/api/user').then((res) => {
        console.log(res.data)
      })
    },
    logout() {
      axios.delete('/api/login').then((res) => {
        console.log(res.data)
      })
    }
  },
  computed: {
    options() {
      return {
        probeType: 3,
        pullDownRefresh: false,
        pullUpLoad: false,
        mouseWheel: true
      }
    }
  }
}
</script>

<style lang="stylus">
@import '~common/stylus/variable'

.account
  width: 100%
  height: 100%
  background-color: $color-background
  .login-wrapper
    display: flex
    align-items: center
    padding: 10px
    background-color: $primary-color
    &:hover
      cursor: pointer
    .account-user
      color: $color-white
      vertical-align: middle
    .title
      height: 40px
      line-height: 40px
      padding-left: 10px
      font-size: 16px
      font-weight: 700
      color: $color-white
    .login-methods
      background-color: $primary-color
  .option-list-content
    width: 100%
    margin-top: 10px
 </style>