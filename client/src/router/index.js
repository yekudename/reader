import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/home'
import Singer from 'components/singer/singer'
import Recommend from 'components/recommend/recommend'
import Search from 'components/search/search'
import SingerDetail from 'components/singer-detail/singer-detail'
import Bookshelf from '@/pages/bookshelf'
import Featured from '@/pages/featured'
import Discover from '@/pages/discover'
import Account from '@/pages/account'
import Category from '@/pages/category'
import Rank from '@/pages/rank'
import BookList from '@/pages/booklist'
import Login from '@/pages/login'
import Register from '@/pages/register'
import User from '@/pages/user'
import Book from '@/pages/book'
import Chapter from '@/pages/chapter'
import ChapterDetail from '@/pages/chapterdetail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Default',
      redirect: '/home/bookshelf'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
      children: [
        {
          path: '/home/bookshelf',
          component: Bookshelf
        },
        {
          path: '/home/featured',
          component: Featured
        },
        {
          path: '/home/discover',
          component: Discover
        },
        {
          path: '/home/account',
          component: Account
        }
      ]
    },
    {
      path: '/category',
      name: 'Category',
      component: Category
    },
    {
      path: '/booklist',
      name: 'BookList',
      component: BookList
    },
    {
      path: '/singer',
      name: 'Singer',
      component: Singer,
      children: [
        {
          path: ':id',
          component: SingerDetail
        }
      ]
    },
    {
      path: '/recommend',
      name: 'Recommend',
      component: Recommend
    },
    {
      path: '/search',
      name: 'Search',
      component: Search
    },
    {
      path: '/rank',
      name: 'Rank',
      component: Rank
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      children: [
        {
          path: '/register',
          name: 'Register',
          component: Register
        }
      ]
    },
    {
      path: '/user',
      name: 'User',
      component: User
    },
    {
      path: '/book/:id',
      name: 'Book',
      component: Book,
      children: [
        {
          name: 'Chapter',
          path: '/book/chapter',
          component: Chapter
        },
        {
          name: 'ChapterDetail',
          path: '/book/chapter/:id',
          component: ChapterDetail
        }
      ]
    }
  ]
})
