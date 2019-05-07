//Displays the comment-reply-form
$(document).ready(function(){

	$('.reply').click(function(e){
		var this_ = $(this);
		var commentID = this_.attr('comment-id');
		var allForms = $('.reply-form');

		//Closes all other open comment-reply-forms
		for (let form of allForms){
			form.style.display = 'none'
		};
		$(`.reply-form[comment-id="${commentID}"]`).css('display', 'flex')
	})
});

//Logic for the cancel button which closes comment-reply-form.
$(document).ready(function(){
	$('.cancel-reply').click(function(e){
		var this_ = $(this);
		var commentID = this_.attr('comment-id');
		$(`.reply-form[comment-id="${commentID}"]`).css('display', 'none');
	})
});

$(document).ready(function(){
	$('.reply-form').submit(function(e){
		e.preventDefault();
		var this_ = $(this);
		var urlEndpoint = this_.attr('action');
		var commentID = this_.attr('comment-id');
		var formData = this_.serialize();

		$.ajax({
			url: urlEndpoint,
			method: 'POST',
			data: formData,
			success: function(response){
				$(`.replies[comment-id="${commentID}"]`).html(response['replies']);
				this_.css('display', 'none');
				$("textarea[name='reply_body']").val('');
			},
		})
	})
})
