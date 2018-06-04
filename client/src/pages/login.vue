<template>
  <div>
    <page class="login">
      <div class="login-header" slot="header">
        <div class="login-header-left" @click="gotoRegister">注册</div>
        <div class="login-header-title">登录</div>
        <div class="login-header-right" @click="back"><i class="fa fa-close"></i></div>
      </div>
      <div class="login-content" slot="content">
        <form method="post" name="login">
          <c-input type="text" placeholder="手机号/邮箱/用户名" v-model="nickName"></c-input>
          <c-input type="password" placeholder="密码" v-model="password"></c-input>
          <c-button type="primary" :long="true" @click="login">登陆</c-button>
        </form>
      </div>
    </page>
    <router-view></router-view>
  </div>
</template>

<script>
import CInput from 'base/input/input'
import Page from 'components/page-template/page-template'
import CButton from 'base/button/button'
import Modal from 'base/modal/modal'
import Radio from 'base/radio/radio'
import RadioGroup from 'base/radio/radio-group'
import Slider from 'base/slider/slider'
import axios from 'api/http'
import {mapMutations, mapGetters} from 'vuex'

export default {
  name: 'login',
  data() {
    return {
      nickName: null,
      password: null,
      userInfo: null,
    }
  },
  computed: {
    ...mapGetters(['token'])
  },
  created() {
    this.getUser()
  },
  methods: {
    login() {
      axios.post('/api/login', {
        nickname: this.nickName,
        password: this.password
      }).then((res) => {
        var data = res.data
        this.setToken(data.data)
      }).catch(err => {
        console.log(err)
      })
    },
    getUser() {
      axios.get('/api/user').then((res) => {
        console.log(res.data)
      })
    },
    gotoRegister() {
      this.$router.replace('/register')
    },
    back() {
      this.$router.back()
    },
    ...mapMutations({
      setToken: 'LOGIN'
    })
  },
  components: {
    CInput,
    Page,
    CButton,
    Modal,
    Radio,
    RadioGroup,
    Slider
  }
}
</script>

<style lang="stylus">
  .login
    position: fixed
    top: 0
    left: 0
    width: 100%
    height: 100%
    .header
      display: block
      .login-header
        display: flex
        align-items: center
        padding: 0 10px
        justify-content: space-between
</style>
