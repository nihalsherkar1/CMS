package com.cms.services;

import com.cms.dto.ProfileDto;
import com.cms.models.User;

public interface UserService {

	public String registerUser(User user);
	
	public ProfileDto getData(User user);
	
	public String updateName(User user);
	
	public String UpdateEmail(User user);
}
