#include <iostream>
#include <memory>
#include <utility>
#include <vector>

class Developer {
 public:
  virtual ~Developer() = default;
  virtual void develop() = 0;
};

class FrontEndDeveloper : public Developer {
 public:
  void develop() override { developFrontEnd(); }

 private:
  void developFrontEnd() {}
};

class BackEndDeveloper : public Developer {
 public:
  void develop() override { developBackEnd(); }

 private:
  void developBackEnd() {}
};

class Project {
 public:
  using Developers = std::vector<std::unique_ptr<Developer>>;
    //Developers is a type alias of a vector of Developer
  explicit Project(Developers developers)
      : developers_{std::move(developers)} {}

  void deliver() {
    for (auto &developer : developers_) {
      developer->develop();
    }
  }

 private:
  Developers developers_;
};

int main() {
  auto developers = Project::Developers{}; //developers is the type alias defined above in class Project
  developers.emplace_back(std::make_unique<FrontEndDeveloper>());
  developers.emplace_back(std::make_unique<BackEndDeveloper>());
  auto project = Project{std::move(developers)};
  project.deliver();
}
