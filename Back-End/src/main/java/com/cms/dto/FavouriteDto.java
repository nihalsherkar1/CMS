package com.cms.dto;

public class FavouriteDto {
	
	private long blogId;
	
	private long userId;

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

	public FavouriteDto(long blogId, long userId) {
		super();
		this.blogId = blogId;
		this.userId = userId;
	}

	public FavouriteDto() {
		super();
	}
	
	

}
