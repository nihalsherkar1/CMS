package com.cms.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cms.dao.UserDao;
import com.cms.dto.ProfileDto;
import com.cms.models.User;

@Service
public class UserServiceImpl implements UserService {
	
	@Autowired
	private UserDao udao;

	@Override
	public String registerUser(User user) {
		
		try {
			user.setRole("ROLE_USER");
			user.setImage("https://cdn-icons-png.flaticon.com/128/3135/3135715.png");
			udao.save(user);
			return "User registered successfully";
		}catch(Exception e){
			return "Something went wrong";
		}
	}

	@Override
	public ProfileDto getData(User user) {
		 long userId=user.getId();
		 ProfileDto pDto=new ProfileDto();
		try {
			 User newUser=udao.findById(userId).orElse(null);
			 
			    if(newUser !=null) {
			    	String image= newUser.getImage();
			    	String name=newUser.getName();
			    	String email=newUser.getEmail();
			    	
			        
			    	pDto.setImage(image);
			    	pDto.setName(name);
			    	pDto.setEmail(email);
			    	pDto.setStatus( 200);
			    	pDto.setMsg("Data Fetched");
			    	return pDto;
			    	
			    }
			    else {
			    	pDto.setStatus(500);
			    	pDto.setMsg("User Not Found");
			    }
			    
			    
		} catch (Exception e) {
			 
			pDto.setStatus(500);
			pDto.setMsg(e.toString());
			
			return pDto;
		}
		
		
		return pDto;
	}

	@Override
	public String updateName(User user) {
		long userId= user.getId();
		
		try {
			User u=udao.findById(userId).orElse(null);
			
			if(u != null){
			 u.setName(user.getName());
			 udao.save(u);
			return "Name Updated Successfull";
				
			}else {
				return "User Not Found";
			}
			
			
		} catch (Exception e) {
			
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public String UpdateEmail(User user) {
		long userId= user.getId();
		try {
			
			User u=udao.findById(userId).orElse(null);
			
			if(u != null) {
				u.setEmail(user.getEmail());
				udao.save(u);
				return "Email Updated Successfull";
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		
		return null;
	}

	
	
	
}
