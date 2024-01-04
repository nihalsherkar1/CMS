package com.cms.dto;

public class CommentDto {
	
	private String comment;
	
	private long blogId;
	
	private long userId;

	public String getComment() {
		return comment;
	}

	public void setComment(String comment) {
		this.comment = comment;
	}

	public long getBlogId() {
		return blogId;
	}

	public void setBlogId(long blogId) {
		this.blogId = blogId;
	}

	public long getUserId() {
		return userId;
	}

	public void setUserId(long userId) {
		this.userId = userId;
	}

	public CommentDto(String comment, long blogId, long userId) {
		super();
		this.comment = comment;
		this.blogId = blogId;
		this.userId = userId;
	}

	public CommentDto() {
		super();
	}
	
	

}
