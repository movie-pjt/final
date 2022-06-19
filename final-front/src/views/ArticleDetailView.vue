<template>
  <div class="container my-5" style="">
    <div class="d-flex flex-column align-items-start article-detail-div py-5 px-5 mb-5 overflow-auto">
      <div class="article-title d-flex justify-content-between">
				<div class="d-flex flex-column mb-2">
					<h1 class="d-flex justfy-content-start">{{ article.title }}</h1>
					<div class="d-flex align-items-end">
						<span class="me-2">{{ article.user.username }}</span>
						<span>{{ getDate(article.created_at) }}</span>
					</div>
				</div>
        <!-- Article Edit/Delete UI -->
        
      <div v-if="isAuthor" class="ed-btn-div d-flex align-items-end mb-2">
        <!-- <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <button>Edit</button>
        </router-link> -->
        
        <font-awesome-icon icon="fa-solid fa-pen-to-square" 
          @click="updateClick"
					class="fa-2x ed-btn"/>
        <font-awesome-icon icon="fa-solid fa-trash-can" 
          @click="deleteArticle(articlePk)"
          class="fa-2x ed-btn"/>
      </div>
      </div>
      <div class="article-content my-3 d-flex flex-column mb-5 text-start">
        {{ article.content }}
      </div>
      <div class="d-flex justify-content-end" style="width:100%">
          <!-- Article Like UI -->
        <div class="d-flex">
          <div>
            <button
              @click="likeArticle(articlePk)"
              class="like-btn d-flex justify-content-center align-items-center">
              <img v-if="isLiked(currentUser.pk)" src="@/assets/img/button_like.png" alt="" style="height: 20px; margin-right:10px;">
              <img v-else src="@/assets/img/button_unlike.png" alt="" style="height: 20px; margin-right:10px;">
              <span>{{ likeCount }}</span>
            </button>
          </div>
        </div>
      </div>
      <comment-list :comments="article.comments"></comment-list>
    </div>
    

    <!-- <p>
      {{ article.content }}
    </p>
    
    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)">Delete</button>
    </div>

    
    <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div>

    <hr /> -->
    
    
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'

  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'currentUser']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ]),
      isLiked(userPk) {
        for (const like_user of this.article.like_users) {
          if (userPk ==like_user.pk) {
            return true
            }
        }
        return false
      },
			getDate: function(dateTimeData) {
				return dateTimeData.split('T')[0]
			},
			updateClick: function() {
				this.$router.push({name: 'updateArticle'})
			}
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
		
  }
</script>

<style>
.article-detail-div {
  background-color: #171717;
  /* border: 1px solid #a0a0a0; */
  border-radius: 20px;
}

.article-content {
  font-family: "Pretendard";
  font-size: 1.3rem;
  height: 70%;
}

.article-title {
  width: 100%;
  border-bottom: 1px solid white;
}

.like-btn {
  height: 35px;
  width: 90px;
  background-color: #202020 !important;
  color: white !important;
  border:white 1px solid !important;
  border-radius: 8px;
}

.like-btn {
  cursor:pointer;
  box-shadow: rgba(255, 255, 255, 0.24) 0px 3px 8px;
  transition: 0.3s;
}
.like-btn:hover {
  box-shadow: rgba(255, 255, 255, 0.24) 0px 9px 19px, rgba(255, 255, 255, 0.24) 0px 7px 6px;
  
}

</style>