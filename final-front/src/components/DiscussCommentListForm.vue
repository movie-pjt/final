<template>
  <form class="comment-list-form d-flex" @submit.prevent>
    <!-- <label for="comment">comment: </label> -->
    <input
    @keyup.enter="onSubmit"
    type="text" id="comment" v-model="content" required
    class="me-3"
    placeholder="댓글을 입력하세요."
    >
    <!-- <button class="comment-btn">Comment</button> -->
    <font-awesome-icon
    @click="onSubmit"
    icon="fa-solid fa-comment" class="fa-2x comment-btn" />
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'DiscussCommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['discuss']),
  },
  methods: {
    ...mapActions(['createDiscussComment']),
    onSubmit() {
      console.log('discuss', this.discuss)
      this.createDiscussComment({ discussPk: this.discuss.pk, content: this.content, })
      this.content = ''
      console.log(this.content)
    }
  }
}
</script>

<style>
.comment-list-form {

  margin: 1rem;
  padding: 1rem;
}

#comment {
  background: none;
  border: none;
  border-bottom: 1px solid white;
  color: white;
  flex-grow: 1;
  font-size: 1.1rem;
}
#comment:focus{
  outline: none;
}



.comment-btn {
  cursor: pointer;
	/* padding: 0px 0px 0px 20px; */
	opacity: 0.5;
  /* width: 20px; */
}

.comment-btn:hover {
	color: white;
	opacity: 1;
}

</style>