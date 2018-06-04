<template>
  <div class="rank">
    <c-button @click="showDialog">
      <div>显示Popup</div>
    </c-button>
    <c-dialog ref="dialog" :title="title" :content="content" :showClose="showClose" type="confirm" :icon="icon">
    </c-dialog>
  </div>
</template>

<script>
import CButton from 'base/button/button'
import CDialog from 'base/dialog/dialog'

export default {
  computed: {
    title() {
      return '标题'
    },
    content() {
      return '就是女急撒看见你u你服务器开始开发看了看迫切我举个卡' +
        '曼橘凯盛家纺i安排foam v你就是女急撒看见你u你服务器开始开发看了看迫切我举个卡曼橘凯盛家纺i安排foam v你'
    },
    showClose() {
      return true
    },
    icon() {
      return 'cubeic-close'
    }
  },
  methods: {
    showDialog() {
      this.$refs.dialog.show()
    }
  },
  components: {
    CButton,
    CDialog
  }
}
</script>
