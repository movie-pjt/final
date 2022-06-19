<template>
  <div class="d-flex align-items-center mb-1 pb-1">
    <li class="comment-list-item mx-3 d-flex justify-content-between">
      <div class="d-flex align-items-center">
        <font-awesome-icon icon="fa-solid fa-user" />
        <div class="mx-1 me-3">
          {{ comment.user.username }}
        </div>
        <span v-if="!isEditing">{{ payload.content }}</span>
        <input v-if="isEditing" type="text" v-model="payload.content">

      </div>
      <div class="d-flex align-items-center">
        <div v-if="isEditing" class="d-flex align-items-center" style="margin-bottom: 2px;">
          <font-awesome-icon icon="fa-solid fa-check"
          @click="onUpdate"
          class="fa-2x ed-btn"/>
          <font-awesome-icon icon="fa-solid fa-xmark"
          @click="switchIsEditing"
          class="fa-2x ed-btn"/>
        </div>
        <span v-if="currentUser.username === comment.user.username && !isEditing">
          <font-awesome-icon icon="fa-solid fa-pen-to-square" 
          @click="switchIsEditing"
          class="fa-2x ed-btn"/>
          <font-awesome-icon icon="fa-solid fa-trash-can" 
          @click="deleteDiscussComment(payload)"
          class="fa-2x ed-btn"/>
        </span>
      </div>
    </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'DiscussCommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        discussPk: this.comment.discuss,
        discussCommentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateDiscussComment', 'deleteDiscussComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateDiscussComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  border-bottom: 1px solid white;
  width: 100%;
  font-size: 1.1rem;
}

.ed-btn {
  cursor: pointer;
	padding: 0px 0px 0px 20px;
	opacity: 0.5;
  width: 20px;
}

.ed-btn:hover {
	color: white;
	opacity: 1;
}
</style>