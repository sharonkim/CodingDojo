Rails.application.routes.draw do
  get 'users/index'

  get 'users/create'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  get '/' => 'users#index'

  post '/create' => 'users#create'
end
