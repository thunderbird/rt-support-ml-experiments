#!/usr/bin/env ruby
require 'rubygems'
require 'bundler/setup'
require 'amazing_print'
require 'time'
require 'date'
require 'logger'
require 'pry'
require 'CSV'
require 'json'

logger = Logger.new($stderr)
logger.level = Logger::DEBUG

if ARGV.length < 2
  puts "usage: #{$PROGRAM_NAME} question_filename.csv answer_filename.csv"
  exit
end

QUESTION_FILENAME = ARGV[0].freeze
ANSWER_FILENAME = ARGV[1].freeze

OUTPUT_FILENAME = "questions-plus-original-poster-answers-and-tags-#{File.basename(QUESTION_FILENAME,
                                                                                   '.*')}.json".freeze
logger.debug("output_filename: #{OUTPUT_FILENAME}")

all_questions = CSV.read(QUESTION_FILENAME, headers: true)
all_answers = CSV.read(ANSWER_FILENAME, headers: true)

all_questions.each do |q|
  content = "#{q['title']} #{q['content']}"
  question_creator = q['creator']
  id = q['id']

  all_answers.select { |a| a['question_id'] == id }.each do |a|
    content += " ... #{a['content']}" if a['creator'] == question_creator
  end
  content += " #{q['tags']}"
  content.downcase!
  logger.debug "question id: #{id}"
end

transformed_data = all_questions.map(&:to_h)
File.open(OUTPUT_FILENAME, 'w') do |f|
  f.puts JSON.pretty_generate(transformed_data)
end
