#model.py
from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy() 

class ProposalStatus(enum.Enum):
    proposed = 1
    accepted = 2
    rejected = 3
    ignored = 4
    reschedule = 5


#one to one relationships

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(String(255))

    #relationships
    profile: Mapped["Profile"] = relationship(back_populates="user")
    matching_preferences: Mapped['MatchingPreferences'] = relationship(back_populates='user')
    sent_proposals: Mapped[list["DateProposal"]] = relationship(back_populates="proposer", foreign_keys="DateProposal.proposer_id")
    received_proposals: Mapped[list["DateProposal"]] = relationship(back_populates="recipient", foreign_keys="DateProposal.recipient_id")
    
    liking: Mapped[list["User"]] = relationship(
        secondary=LikingAssociation.__table__,
        primaryjoin=LikingAssociation.liker_id == id,
        secondaryjoin=LikingAssociation.liked_id == id,
        back_populates="likers", #make sure liking is right
    )
    likers: Mapped[list["User"]] = relationship(
        secondary=LikingAssociation.__table__,
        primaryjoin=LikingAssociation.liked_id == id,
        secondaryjoin=LikingAssociation.liker_id == id,
        back_populates="liking", #make sure likers is right
    )
    blocking: Mapped[list["User"]] = relationship(
        secondary=BlockingAssociation._table_,
        primaryjoin=BlockingAssociation.blocker_id == id,
        secondaryjoin=BlockingAssociation.blocked_id == id,
        back_populates="blockers", #MAKE SURE blocking is right
    )
    blockers: Mapped[list["User"]] = relationship(
        secondary=BlockingAssociation._table_,
        primaryjoin=BlockingAssociation.blocked_id == id,
        secondaryjoin=BlockingAssociation.blocker_id == id,
        back_populates="blocking", #MAKE SURE blockers is right
    )

# Users are identified by an email and they authenticate with a password, 
# which has to be stored salted and encrypted in the database. 
# Users will also have their profile information and their matching preferences. 
# There are two many to many relationships between users: 
# A user can like (or block) many users, and a user can be liked (or blocked) by many users.


class Profile(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), unique=True)
    user: Mapped["User"] = relationship(
        back_populates="profile",
        single_parent=True,
    )
    photo_id: Mapped[int] = mapped_column(ForeignKey("photo.id"))
    photo: Mapped[Optional["Photo"]] = relationship(back_populates="profile")


class Photo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped["Profile"] = relationship(back_populates="photo")
    file_extension: Mapped[str] = mapped_column(String(8))

# many to many 


class LikingAssociation(db.Model):
    liker_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    liked_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)



#one to many relationships





