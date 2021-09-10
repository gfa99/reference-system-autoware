// Copyright 2021 Apex.AI, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

#include <chrono>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "reference_system/node_settings.hpp"
#include "reference_system/sample_management.hpp"
#include "reference_system/types.hpp"

namespace reference_nodes {
class Sensor : public rclcpp::Node {
 public:
  Sensor(const SensorSettings& settings) : Node(settings.node_name) {
    publisher_ = this->create_publisher<message_t>(settings.topic_name, 10);
    timer_ = this->create_wall_timer(settings.cycle_time,
                                     [this] { timer_callback(); });
  }

 private:
  void timer_callback() {
    auto message = publisher_->borrow_loaned_message();
    message.get().size = 0;

    set_sample(this->get_name(), message.get());

    publisher_->publish(std::move(message));
  }

 private:
  rclcpp::Publisher<message_t>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};
}  // namespace reference_nodes
