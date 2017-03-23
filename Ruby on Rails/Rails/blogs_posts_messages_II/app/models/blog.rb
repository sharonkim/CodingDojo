class Blog < ApplicationRecord
    has_many :owners
    has_many :posts
    has_many :users, through :owners
    has many :user_poasts, through: :posts, source: user_poasts

    validates :name, :description, presence: true
end
