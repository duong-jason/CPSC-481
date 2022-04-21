% Lecture_1

% Clause/Fact :- <Predicate>(<Atoms>).

% Rule :- <Conclusion> :- <Condition>.
% Conclusion :- <Predicate>(Variable)
% Condition :- <Predicate>(Variable)
%           |  <Predicate>(Variable), <Condition>

% Atoms :- <Value>
% Variables :- <Capital>
%           | _<Capital>


parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

% Prove Fact
%   ?- parent(bob, pat) -> True
%   ?- parent(liz, pat) -> False
%   ?- parent(tom, ben) -> False 

% Get All Pairs
%   parent(X, Y)

% Get Parent/Children/Grandparent/Grandchildren
%   parent(X, liz) -> tom
%   parent(bob, X) -> ann, pat
%   parent(Y, jim), parent(X, Y) -> X=bob, Y=pat
%   parent(tom, X), parent(X, Y) -> X=bob, Y=ann | X=bob, Y=pat

% Common Parent
%   parent(X, ann), parent(X, pat) -> bob

female(pam).
female(liz).
female(ann).
female(pat).
male(tom).
male(bob).
male(jim).

child(Y, X) :- parent(X, Y).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sister(X, Y) :- parent(P, X), parent(P, Y), female(X).
