import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
    state: {
        articles: [],
        article: {},
    },

    getters: {
        articles: state => state.articles,
        article: state => state.article,
        isAuthor: (state, getters) => {
            return state.article.user?.username === getters.currentUser.username
        },
        isArticle: state => !_.isEmpty(state.article),
    },

    mutations: {
        SET_ARTICLES: (state, articles) => state.articles = articles,
        SET_ARTICLE: (state, article) => state.article = article,
        SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments),
    },

    actions: {
        // 게시글 목록 받아오기 - GET: articles URL (token)
        fetchArticles({ commit, getters}) {
            axios({
                url: drf.articles.articles(),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_ARTICLES', res.data))
            .catch(err => console.error(err.response))
        },

        // 단일 게시글 받아오기
        fetchArticle({ commit, getters }, articlePk) {
            axios({
                url: drf.articles.article(articlePk),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_ARTICLE', res.data))
            .catch(err => {
                console.error(err.response)
                if (err.response.status === 404) {
                    router.push({ name: 'NotFound404' })
                }
            })
        },

        // 게시글 생성 - POST: articles URL (게시글 입력 정보, token)
        createArticle({ commit, getters }, article) {
            axios({
                url: drf.articles.articles(),
                method: 'post',
                data: article,
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_ARTICLE', res.data)
                router.push({
                    name: 'article',
                    params: { articlePk: getters.article.pk }
                })
            })
        },

        // 게시글 수정 - PUT: article URL (게시글 입력 정보, token)
        updateArticle({ commit, getters }, { pk, title, content}) {
            axios({
                url: drf.articles.article(pk),
                method: 'put',
                data: { title, content},
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_ARTICLE', res.data)
                router.push({
                    name: 'article',
                    params: { articlePk: getters.article.pk }
                })
            })
        },

        // 게시글 삭제 - DELETE: article URL (token)
        deleteArticle({ commit, getters }, articlePk) {
            if (confirm('정말 삭제하시겠습니까?')) {
                axios({
                    url: drf.articles.article(articlePk),
                    method: 'delete',
                    headers: getters.authHeader,
                })
                .then(() => {
                    commit('SET_ARTICLE', {})
                    router.push({ name: 'articles'})
                })
                .catch(err => console.error(err.response))
            }
        },

        // 좋아요 - POST: likeArticle URL(token)
        likeArticle({ commit, getters}, articlePk) {
            axios({
                url: drf.articles.likeArticle(articlePk),
                method: 'post',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_ARTICLE', res.data))
            .catch(err => console.error(err.response))
        },

        // 댓글 생성 - POST: comments URL(댓글 입력 정보, token)
        createComment({ commit, getters }, { articlePk, content }) {
            const comment = { content }

            axios({
                url: drf.articles.comments(articlePk),
                method: 'post',
                data: comment,
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_ARTICLE_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        },

        // 댓글 수정 - PUT: comment URL(댓글 입력 정보, token)
        updateComment({ commit, getters }, {articlePk, commentPk, content}) {
            const comment = { content }

            axios({
                url: drf.articles.comment(articlePk, commentPk),
                method: 'put',
                data: comment,
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_ARTICLE_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        },

        // 댓글 삭제 - DELETE: comment URL (token)
        deleteComment({ commit, getters }, { articlePk, commentPk }) {
            if (confirm('정말 삭제하시겠습니까?')) {
                axios({
                    url: drf.articles.comment(articlePk, commentPk),
                    method: 'delete',
                    data: {},
                    headers: getters.authHeader,
                })
                .then(res => {
                    commit('SET_ARTICLE_COMMENTS', res.data)
                })
                .catch(err => console.error(err.response))
            }
        },
    },
}