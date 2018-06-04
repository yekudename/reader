<template>
  <page class="register">
    <div class="register-header" slot="header">
      <div class="register-header-left" @click="gotoLogin">登录</div>
      <div class="register-header-title">注册</div>
      <div class="register-header-right" @click="back"><i class="fa fa-close"></i></div>
    </div>
    <div class="register-content" slot="content">
    <form>
        <c-input type="text" placeholder="用户名" v-model="nickname"></c-input>
        <c-input type="password" placeholder="密码" v-model="password"></c-input>
        <c-button type="primary" :long="true" @click="submit">注册</c-button>
    </form>
    </div>
  </page>
</template>

<script>
import CInput from 'base/input/input'
import Page from 'components/page-template/page-template'
import CButton from 'base/button/button'
import { register } from 'api/getdata'

export default {
  name: 'register',
  data() {
    return {
      nickname: '',
      password: '',
      userInfo: null
    }
  },
  methods: {
    async submit() {
      this.userInfo = await register(this.nickname, this.password)
      console.log(this.userInfo)
    },
    gotoLogin() {
      this.$router.replace('/login')
    },
    back() {
      this.$router.back()
    }
  },
  components: {
    CInput,
    Page,
    CButton
  }
}
</script>

<style lang="stylus">
  .register
    position: fixed
    top: 0
    left: 0
    width: 100%
    height: 100%
    .header
      display: block
      .register-header
        display: flex
        align-items: center
        padding: 0 10px
        justify-content: space-between
</style>