import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
    state: {
        discusses: [],
        discuss: {},
    },

    getters: {
        discusses: state => state.discusses,
        discuss: state => state.discuss,
        isDiscussAuthor: (state, getters) => {
            return state.discuss.user?.username === getters.currentUser.username
        },
        isdiscuss: state => !_.isEmpty(state.discuss),
    },

    mutations: {
        SET_discusses: (state, discusses) => state.discusses = discusses,
        SET_DISCUSS: (state, discuss) => state.discuss = discuss,
        SET_DISCUSS_COMMENTS: (state, comments) => (state.discuss.discuss_comments = comments),
    },

    actions: {
        // 게시글 목록 받아오기 - GET: discusses URL (token)
        fetchdiscusses({ commit, getters }) {
            axios({
                url: drf.discuss.discusses(),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => {commit('SET_discusses', res.data)
        })
            .catch(err => console.error(err.response))
        },

        // 단일 게시글 받아오기
        fetchdiscuss({ commit, getters }, discussPk) {
            axios({
                url: drf.discuss.discuss(discussPk),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_DISCUSS', res.data)
            })
            .catch(err => {
                console.error(err.response)
                if (err.response.status === 404) {
                    router.push({ name: 'NotFound404' })
                }
            })
        },
        discussChoice({ commit, getters}, {discussPk, choice}) {
            let choiceUrl
            if (choice === 'A'){
                choiceUrl = drf.discuss.discussChoiceA(discussPk)
            } else if (choice === 'B') {
                choiceUrl = drf.discuss.discussChoiceB(discussPk)
            }
            console.log(discussPk, choice, choiceUrl)
            axios({
                url: choiceUrl,
                method: 'post',
                headers: getters.authHeader,
            })
            .then(res => commit('SET_DISCUSS', res.data))
            .catch(err => {
                console.log('error')
                console.error(err.response)})
        },
        createDiscussComment({ commit, getters }, { discussPk, content }) {
            const comment = { content }

            axios({
                url: drf.discuss.discussComments(discussPk),
                method: 'post',
                data: comment,
                headers: getters.authHeader,
            })
            .then(res => {
                console.log('discussCommentCreate!')
                commit('SET_DISCUSS_COMMENTS', res.data)
        })
            .catch(err => console.error(err.response))
        },
        updateDiscussComment({ commit, getters }, {discussPk, discussCommentPk, content}) {
            const comment = { content }

            axios({
                url: drf.discuss.discussComment(discussPk, discussCommentPk),
                method: 'put',
                data: comment,
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_DISCUSS_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        },
        deleteDiscussComment({ commit, getters }, { discussPk, discussCommentPk }) {
            if (confirm('정말 삭제하시겠습니까?')) {
                axios({
                    url: drf.discuss.discussComment(discussPk, discussCommentPk),
                    method: 'delete',
                    data: {},
                    headers: getters.authHeader,
                })
                .then(res => {
                    commit('SET_DISCUSS_COMMENTS', res.data)
                })
                .catch(err => console.error(err.response))
            }
        },
    },
}