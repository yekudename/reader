<template>
  <page>
    <div slot="content" v-if="user">
      <span>{{user.id}}</span>
      <span>{{user.nickname}}</span>
      <span>{{user.phone}}</span>
      <span>{{user.email}}</span>
      <span>{{user.city}}</span>
      <span>{{user.province}}</span>
    </div>
  </page>
</template>

<script>
import {user} from 'api/getdata'
import CInput from 'base/input/input'
import Page from 'components/page-template/page-template'

export default {
  data() {
    return {
      user: null
    }
  },
  created() {
    this.getUserById(1)
  },
  methods: {
    async getUserById(userid) {
      this.user = await user(userid)
    }
  },
  components: {
    CInput,
    Page
  }
}
</script>