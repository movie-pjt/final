<template>
  <div class="container">
    <div
    class="d-flex flex-column align-items-start article-detail-div py-5 px-5 mb-5 overflow-auto"
    style="width:100%"
    >
      <div class="create-title py-3 d-flex justify-content-between mb-3"
      style="width:100%"
      >
        <form @submit.prevent="onSubmit" style="width:100%">
          <div
          style="width:100%"
          class="d-flex flex-column align-items-start"
          >
            <label for="title" class="mb-2" style="font-family: 'Pretendard'; font-size: 20px;">제목</label>
            <b-form-input v-model="newArticle.title" type="text" id="title" required/>
          </div>
          <div
          style="width:100%"
          class="d-flex flex-column align-items-start"
          >
            <label for="content" class="my-2" style="font-family: 'Pretendard'; font-size: 20px;">내용</label>
            <b-form-textarea v-model="newArticle.content" type="text" id="content" style="height: 300px" required></b-form-textarea>
          </div>
          <div>
            <button class="article-btn mt-3">{{ action }}</button>
          </div>
        </form>
      </div>
    </div>
  </div>



</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'CREATE') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'UPDATE') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style>

.article-btn {
  width: 80px;
	height: 50px;
	text-align: center;
	font-family: 'Pretendard';
	font-weight: 700;
	border-radius: 7px;
  border-color: #E9BA13;
	transition: 0.5s;
  box-shadow: rgba(255, 255, 255, 0.24) 0px 3px 8px;
  transition: 0.3s;
}

.article-btn:hover {
	background: #E9BA13;
  box-shadow: rgba(255, 255, 255, 0.24) 0px 9px 19px, rgba(255, 255, 255, 0.24) 0px 7px 6px;
}

</style>
