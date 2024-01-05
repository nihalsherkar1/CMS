package com.cms.dto;

public class ProfileDto {

	private String image;
	private String name;
	private String email;
	
	private String msg;
	private Integer status;
	
	
	public ProfileDto() {
		super();
	 
	}
	 
	public ProfileDto(String image, String name, String email, String msg, Integer status) {
		super();
		this.image = image;
		this.name = name;
		this.email = email;
		this.msg = msg;
		this.status = status;
	}

	public String getImage() {
		return image;
	}
	public void setImage(String image) {
		this.image = image;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
	
	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}

	public Integer getStatus() {
		return status;
	}

	public void setStatus(Integer status) {
		this.status = status;
	}

	@Override
	public String toString() {
		return "ProfileDto [image=" + image + ", name=" + name + ", email=" + email + ", msg=" + msg + ", status="
				+ status + "]";
	}

	 
	
	
}
