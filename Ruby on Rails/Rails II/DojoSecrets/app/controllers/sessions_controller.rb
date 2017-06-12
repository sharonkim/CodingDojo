class SessionsController < ApplicationController
    before_action :require_login, except: [:new, :create]

    def new
    end

    def create
        @user = User.find_by_email(params[:email])
        if user && @user.authenticate(params[:password])
            session[:user_id] = @user.id
            redirect_to "/users/#{@user.id}", notice "You have been successfully logged in."

        else
            flash[:errors] = ["Invalid Email or Password.  Please try again."]
            redirect_to "/sessions/new"
        end
    end

    def destroy
        reset_session
        redirect_to "/sessions/new"
    end
end
