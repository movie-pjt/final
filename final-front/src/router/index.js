import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import CommunityView from '../views/CommunityView.vue'
import ArticleListView from '../views/ArticleListView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ArticleUpdateView from '../views/ArticleUpdateView.vue'
import DiscussView from '../views/DiscussView.vue'
import DiscussDetailView from '../views/DiscussDetailView.vue'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'articleCreate',
    component: ArticleCreateView
  },
  {
    path: '/articles/:articlePk/update',
    name: 'updateArticle',
    component: ArticleUpdateView
  },
  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/movies',
    name: 'movies',
    component: MovieView,
    children: [
      {
        name: 'movie_detail',
        path: '/movies/:moviePk'
      }
    ]
  },
  {
    path: '/discuss',
    name: 'discuss',
    component: DiscussView
  },
  {
  path: '/discuss/:discussPk',
  name: 'discussDetail',
  component: DiscussDetailView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  // {
  //   path: '*',
  //   redirect: '/404'
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  store.getters.c
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup', 'home', 'movies']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인이 필요합니다!')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next()
  }
})

export default router
